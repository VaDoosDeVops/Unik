import threading

from config import print


# Функция для выполнения с таймаутом
def run_with_timeout(func, timeout, *args, **kwargs):
    timeout += 300
    result = [None]  # Для хранения результата

    def target():
        result[0] = func(*args, **kwargs)

    thread = threading.Thread(target=target)
    thread.start()
    thread.join(timeout)  # Ожидаем выполнение с таймаутом

    if thread.is_alive():
        print(f"Функция difflib не завершилась за {timeout} секунд.")
        return None
    return result[0]
