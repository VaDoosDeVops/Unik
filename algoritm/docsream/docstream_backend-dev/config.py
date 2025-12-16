text_upload_folder = 'uploads/'
text_result_folder = 'results/'

spreadsheet_upload_folder = 'uploads/'
spreadsheet_result_folder = 'results/'


import logging
import sys

# Настраиваем базовый логгер
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),  # Отправляем логи в stdout
    ]
)

logger = logging.getLogger(__name__)
print = logger.info