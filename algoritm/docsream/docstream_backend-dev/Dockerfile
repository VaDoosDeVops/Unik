# Используем официальный образ Python как базовый
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-rus \
    libtesseract-dev \
    libreoffice \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*
    
# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# Копируем весь код приложения в рабочую директорию
COPY . .

# Открываем порт, на котором будет работать приложение
EXPOSE 5000

# Определяем переменную окружения для Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Запускаем приложение
CMD ["flask", "run"]
