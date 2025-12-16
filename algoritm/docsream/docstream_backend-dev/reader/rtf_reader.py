import os
import subprocess

from docx import Document
from docx.text.run import Run
from striprtf.striprtf import rtf_to_text

from file_utils import create_document_and_map

LIBRE_PATH = os.getenv("LIBRE_PATH")

from config import text_upload_folder as text_uf

def read_rtf(file_path) -> (str, Document, dict[int, Run]):
    """
    Старая реализация. Не читает таблицы и фото
    """
    with open(file_path, 'r') as f:
        content = f.read()
        text = rtf_to_text(content)
    doc, index_map = create_document_and_map(text)
    return text, doc, index_map

def convert_rtf_to_docx(file_path) -> (str, Document, dict[int, Run]):
    subprocess.run([LIBRE_PATH, '--headless', '--convert-to', 'docx', file_path, '--outdir', './' + text_uf])
    return file_path.replace('.rtf', '.docx')
