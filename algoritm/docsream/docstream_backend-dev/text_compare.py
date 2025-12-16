import time
from functools import lru_cache

from docx.enum.text import WD_COLOR_INDEX

from config import print
from config import spreadsheet_result_folder as result_folder
from config import spreadsheet_upload_folder as upload_folder
from difference_finder import find_text_differences_dmp, find_text_differences_difflib
from file_utils import *
from reader.docx_reader import read_docx_with_tables, read_doc
from reader.pdf_reader import read_pdf_with_tables
from reader.rtf_reader import convert_rtf_to_docx
from timeout_runner import run_with_timeout


def __save_result_file_as_docx(file, filename):
    filename = filename.split('.', 1)[0] + '.docx'
    path = os.path.join(result_folder, filename)
    file.save(path)
    print('Result saved in: ' + path)
    return filename


@lru_cache(maxsize=128)
def read_file(filename):
    file_path = os.path.join(upload_folder, filename)
    match get_file_format(filename):
        case 'docx':
            text, doc, index_map = read_docx_with_tables(file_path)
        case 'doc':
            text, doc, index_map = read_doc(file_path)
        case 'pdf':
            text, doc, index_map = read_pdf_with_tables(file_path)
        case 'txt':
            text, doc, index_map = read_txt(file_path)
        case 'rtf':
            file_path = convert_rtf_to_docx(file_path)
            text, doc, index_map = read_docx_with_tables(file_path)
        case _:
            raise ValueError('Unsupported file format')
    return text, doc, index_map


def highlight_text(indices, color, index_map):
    """
    Highlights characters at the specified indices in the given color.
    """
    for idx in indices:
        run = index_map.get(idx, None)
        if run is not None:
            run.font.highlight_color = color


def apply_highlights(differences, color_map, index_map):
    """
    Apply highlights to the document based on differences and color map.
    """
    for change_type, color in color_map.items():
        highlight_text(differences[change_type], color, index_map)


def _get_differences(text1, text2):
    start_time = time.time()
    differences_dmp = find_text_differences_dmp(text1, text2)
    dmp_execution_time = time.time() - start_time
    print(f"Время выполнения diff_match_patch {dmp_execution_time} секунд")
    if dmp_execution_time < 0.0005:
        # если dmp выполнилось быстрее 0.5 миллисекунд - бан
        print("Выбрана difflib для показа изменений")
        start_time = time.time()
        differences_difflib = find_text_differences_difflib(text1, text2)
        difflib_execution_time = time.time() - start_time
        print(f"Время выполнения difflib {difflib_execution_time} секунд")
        return differences_difflib

    start_time = time.time()
    differences_difflib = run_with_timeout(find_text_differences_difflib, dmp_execution_time + 5, text1, text2)
    difflib_execution_time = time.time() - start_time
    if differences_difflib is None:
        # если difflib выполнялось дольше dmp +5 секунд - бан
        print("Выбрана diff_match_patch для показа изменений")
        return differences_dmp
    print(f"Время выполнения difflib {difflib_execution_time} секунд")

    # выбираем того, у кого меньше изменений
    len_difflib = sum(len(t) for t in differences_difflib.values())
    len_dmp = sum(len(t) for t in differences_dmp.values())
    if len_difflib < len_dmp:
        print("Выбрана difflib для показа изменений")
        return differences_difflib
    else:
        print("Выбрана diff_match_patch для показа изменений")
        return differences_dmp


def compare_and_save(filename1, filename2):
    text1, doc1, index_map1 = read_file(filename1)
    text2, doc2, index_map2 = read_file(filename2)

    differences = _get_differences(text1, text2)

    # Define colors
    red = WD_COLOR_INDEX.RED
    yellow = WD_COLOR_INDEX.YELLOW
    green = WD_COLOR_INDEX.BRIGHT_GREEN

    # Apply highlights
    color_map1 = {
        'removed_text1': red,
        'changed_text1': yellow
    }

    color_map2 = {
        'added_text2': green,
        'changed_text2': yellow
    }

    apply_highlights(differences, color_map1, index_map1)
    apply_highlights(differences, color_map2, index_map2)

    # Save the modified documents
    filename1 = __save_result_file_as_docx(doc1, filename1)
    filename2 = __save_result_file_as_docx(doc2, filename2)

    # закомментить на проде
    # for el in differences:
    #     print(el, differences[el])

    return filename1, filename2
