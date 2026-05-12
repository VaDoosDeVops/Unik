from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__, template_folder='templates', static_folder='static')
OVERPASS_URLS = [
    'https://overpass.kumi.systems/api/interpreter',
    'https://lz4.overpass-api.de/api/interpreter',
    'https://overpass.openstreetmap.fr/api/interpreter',
    'https://overpass-api.de/api/interpreter',
]
OVERPASS_HEADERS = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (compatible; OpenStreetMap overpass client)',
}

SEARCH_FILTERS = [
    ('shop', 'supermarket'),
    ('shop', 'convenience'),
    ('shop', 'mall'),
    ('shop', 'kiosk'),
    ('shop', 'bakery'),
    ('shop', 'department_store'),
    ('amenity', 'supermarket'),
    ('amenity', 'convenience'),
    ('amenity', 'fuel'),
    ('amenity', 'pharmacy'),
]


def build_overpass_query(lat, lon, radius):
    body = []
    for key, value in SEARCH_FILTERS:
        body.append(f'node["{key}"="{value}"]["opening_hours"](around:{radius},{lat},{lon});')
        body.append(f'way["{key}"="{value}"]["opening_hours"](around:{radius},{lat},{lon});')
        body.append(f'relation["{key}"="{value}"]["opening_hours"](around:{radius},{lat},{lon});')

    q = '[out:json][timeout:25];(' + ''.join(body) + ');out center tags;'
    return q


def fetch_overpass_data(query):
    for endpoint in OVERPASS_URLS:
        try:
            response = requests.post(endpoint, data={'data': query}, headers=OVERPASS_HEADERS, timeout=30)
        except requests.RequestException as exc:
            continue
        if response.status_code == 200:
            return response
        # если endpoint вернул не 200, пробуем следующий
    return None


def parse_time(value):
    if not value:
        return None
    value = value.strip()
    if value == '24/7':
        return 24 * 60
    try:
        hours, minutes = value.split(':')
        return int(hours) * 60 + int(minutes)
    except Exception:
        return None


def is_open_at_21(opening_hours):
    if not opening_hours:
        return False
    text = opening_hours.lower()
    if '24/7' in text or 'круглосуточно' in text or '24 часа' in text:
        return True

    ranges = re.findall(r'(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})', text)
    if not ranges:
        if 'open' in text and 'close' not in text:
            return True
        return False

    target = 21 * 60
    for start, end in ranges:
        start_min = parse_time(start)
        end_min = parse_time(end)
        if start_min is None or end_min is None:
            continue
        if start_min <= end_min:
            if start_min <= target < end_min or target == start_min:
                return True
        else:
            if target >= start_min or target < end_min:
                return True
    return False


def extract_coords(element):
    if 'lat' in element and 'lon' in element:
        return element['lat'], element['lon']
    if 'center' in element:
        center = element['center']
        return center.get('lat'), center.get('lon')
    return None, None


def haversine(lat1, lon1, lat2, lon2):
    from math import radians, cos, sin, asin, sqrt
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    return 6371000 * c


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/shops')
def api_shops():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    radius = request.args.get('radius', '2000')

    try:
        lat = float(lat)
        lon = float(lon)
        radius = int(radius)
    except (TypeError, ValueError):
        return jsonify({'error': 'Неверные параметры координат или радиуса.'}), 400

    query = build_overpass_query(lat, lon, radius)
    response = fetch_overpass_data(query)
    if response is None:
        return jsonify({'error': 'Все Overpass-серверы недоступны или вернули ошибку.'}), 502

    try:
        data = response.json()
    except ValueError:
        return jsonify({'error': 'Ошибка разбора ответа от Overpass API.'}), 502
    elements = data.get('elements', [])
    shops = []

    for element in elements:
        tags = element.get('tags', {})
        opening_hours = tags.get('opening_hours', '')
        if not is_open_at_21(opening_hours):
            continue

        lat_item, lon_item = extract_coords(element)
        distance = None
        if lat_item is not None and lon_item is not None:
            distance = haversine(lat, lon, lat_item, lon_item)

        shops.append({
            'id': element.get('id'),
            'type': element.get('type'),
            'lat': lat_item,
            'lon': lon_item,
            'tags': tags,
            'distance': distance,
        })

    shops = sorted(shops, key=lambda x: x['distance'] if x['distance'] is not None else float('inf'))
    return jsonify({'shops': shops})


if __name__ == '__main__':
    app.run(debug=True)
