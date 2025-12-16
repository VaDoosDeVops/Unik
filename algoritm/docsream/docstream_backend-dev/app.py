import os

import nltk
from dotenv import load_dotenv
from flask import Flask, request, render_template, send_file, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

import spreadsheet_compare
import text_compare
from config import print
from converter import convert_xls2xlsx
from file_utils import is_filename_secured, get_uploaded_file, ALLOWED_TEXT_EXT, generate_new_filename, \
    save_uploaded_file, ALLOWED_SPREADSHEET_EXT
from spreadsheet_compare import upload_folder as spreadsheet_uf, result_folder as spreadsheet_rf
from text_compare import get_file_format
from text_compare import upload_folder as text_uf, result_folder as text_rf

load_dotenv()
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS").split(',')
nltk.download('wordnet')
nltk.download('punkt')

app = Flask(__name__)
CORS(app, origins=ALLOWED_ORIGINS, methods=['GET', 'POST'], headers=['Content-Type', 'Authorization'])
os.makedirs(text_uf, exist_ok=True)
os.makedirs(text_rf, exist_ok=True)
os.makedirs(spreadsheet_uf, exist_ok=True)
os.makedirs(spreadsheet_rf, exist_ok=True)


@cross_origin(origins=ALLOWED_ORIGINS)
@app.route('/')
def index():
    return render_template('index.html')


def compare_files(filename1, filename2):
    if get_file_format(filename1) in ALLOWED_SPREADSHEET_EXT and get_file_format(filename2) in ALLOWED_SPREADSHEET_EXT:
        if get_file_format(filename1) == 'xls':
            filename1 = convert_xls2xlsx(filename1)
        if get_file_format(filename2) == 'xls':
            filename2 = convert_xls2xlsx(filename2)
        spreadsheet_compare.compare_and_save(filename1, filename2)
    elif get_file_format(filename1) in ALLOWED_TEXT_EXT and get_file_format(filename2) in ALLOWED_TEXT_EXT:
        filename1, filename2 = text_compare.compare_and_save(filename1, filename2)
    else:
        return "File types should be comparable", 400

    response_data = {'filename1': filename1, 'result1': "<div><span>nothing</span></div>", 'filename2': filename2,
                     'result2': "<div><span>nothing</span></div>"}
    return response_data


@cross_origin(origins=ALLOWED_ORIGINS)
@app.route('/compare', methods=['GET'])
def compare():
    filename1 = request.args.get('file1')
    filename2 = request.args.get('file2')

    if not filename1 or not filename2:
        return 'Please provide both names', 400

    if not is_filename_secured(filename1):
        return 'Bad filename for file1', 400

    if not is_filename_secured(filename2):
        return 'Bad filename for file2', 400

    file1 = get_uploaded_file(filename1)
    file2 = get_uploaded_file(filename2)

    if not file1:
        return f'File {filename1} not found', 400

    if not file2:
        return f'File {filename2} not found', 400

    return jsonify(compare_files(filename1, filename2)), 200


@cross_origin(origins=ALLOWED_ORIGINS)
@app.route('/download', methods=['GET'])
def download_file():
    filename = request.args.get('filename')
    if not filename:
        return 'No filename provided', 400
    if not is_filename_secured(filename):
        return 'Bad filename', 400
    try:
        if get_file_format(filename) in ALLOWED_TEXT_EXT:
            file = os.path.join(text_rf, filename)
        else:
            file = os.path.join(spreadsheet_rf, filename)
        response = send_file(file, as_attachment=True, download_name=filename)
        response.headers["Access-Control-Expose-Headers"] = "Content-Disposition"
        print(f"File downloaded successfully: {filename}")
        return response
    except FileNotFoundError:
        return 'File not found', 404


@cross_origin(origins=ALLOWED_ORIGINS)
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not file:
        return 'Please select a file', 400
    if not is_filename_secured(file.filename):
        return 'Bad filename', 400

    file.filename = secure_filename(generate_new_filename(file.filename))

    filename = save_uploaded_file(file)
    return jsonify({'filename': filename}), 200


if __name__ == '__main__':
    app.run(debug=True)
