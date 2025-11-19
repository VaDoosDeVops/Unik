from flask import Flask, render_template, request, jsonify, send_file
from PIL import Image, ImageDraw, ImageEnhance
import numpy as np
import os
import io

app = Flask(__name__)


# Функция для генерации паттернов
def generate_patterns():
    patterns = []
    for i in range(10):
        pattern = Image.new('1', (10, 10), 1)
        draw = ImageDraw.Draw(pattern)
        if i == 0:
            pass  # Самый темный - без точек
        elif i == 1:
            draw.point((5, 5), fill=0)
        elif i == 2:
            draw.point((3, 3), fill=0)
            draw.point((7, 7), fill=0)
        elif i == 3:
            draw.line((0, 0, 9, 9), fill=0)
        elif i == 4:
            draw.line((0, 9, 9, 0), fill=0)
        elif i == 5:
            draw.rectangle([2, 2, 7, 7], outline=0)
        elif i == 6:
            draw.ellipse([2, 2, 7, 7], outline=0)
        elif i == 7:
            for x in range(0, 10, 2):
                draw.line((x, 0, x, 10), fill=0)
        elif i == 8:
            for y in range(0, 10, 2):
                draw.line((0, y, 10, y), fill=0)
        elif i == 9:
            draw.line((0, 0, 9, 9), fill=0)
            draw.line((0, 9, 9, 0), fill=0)
        patterns.append(pattern)
    return patterns


# Функция для обработки изображения с паттернами
def process_image_with_patterns(image, contrast_value=1.0, square_size=10, invert_colors=False):
    img = image.convert('L')  # Преобразуем в черно-белый формат
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast_value)  # Изменение контраста

    width, height = img.size
    # Устанавливаем цвет фона: (0, 0, 0) - черный, (255, 255, 255) - белый
    bg_color = (0, 0, 0) if invert_colors else (255, 255, 255)
    fg_color = (255, 255, 255) if invert_colors else (0, 0, 0)

    # Создаем изображение с указанным фоном
    processed_img = Image.new('RGB', (width, height), bg_color)
    patterns = generate_patterns()

    # Если инверсированы цвета, инвертируем порядок паттернов
    if invert_colors:
        patterns = patterns[::-1]

    # Применение паттернов
    for x in range(0, width, square_size):
        for y in range(0, height, square_size):
            box = (x, y, x + square_size, y + square_size)
            region = img.crop(box)
            avg_brightness = np.mean(np.array(region))

            # Определяем индекс паттерна на основе яркости
            pattern_index = len(patterns) - 1 - int(avg_brightness // (256 / len(patterns)))
            pattern = patterns[pattern_index]

            # Конвертируем паттерн в RGB для работы с цветами
            pattern_rgb = pattern.convert("RGB")
            for i in range(pattern.size[0]):
                for j in range(pattern.size[1]):
                    if pattern.getpixel((i, j)) == 0:  # Если пиксель черный
                        pattern_rgb.putpixel((i, j), fg_color)  # Меняем на цвет fg_color
                    else:
                        pattern_rgb.putpixel((i, j), bg_color)  # Остальные на цвет bg_color

            processed_img.paste(pattern_rgb, (x, y))

    return processed_img



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    if file:
        filepath = os.path.join('static', 'uploads', file.filename)
        file.save(filepath)
        return jsonify({'filepath': filepath})


@app.route('/process', methods=['POST'])
def process_image():
    data = request.json
    filepath = data.get('filepath')
    contrast = float(data.get('contrast', 1.0))
    invert_colors = data.get('invert_colors', False)  # Получаем параметр для инверсии цветов

    if filepath and os.path.exists(filepath):
        img = Image.open(filepath)
        processed_img = process_image_with_patterns(img, contrast_value=contrast, invert_colors=invert_colors)

        # Сохраняем изображение в поток байтов
        img_io = io.BytesIO()
        processed_img.save(img_io, 'PNG')
        img_io.seek(0)

        # Отправляем файл в ответе
        return send_file(img_io, mimetype='image/png')

    return jsonify({'error': 'Invalid file'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)