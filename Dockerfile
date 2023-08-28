# Используем официальный образ Python
FROM python:3.9-slim

# Установка рабочей директории в контейнере
WORKDIR /app

# Установка переменных окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка зависимостей
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копирование проекта в контейнер
COPY . /app/

# Указываем команду для запуска при старте контейнера
CMD ["python", "bot/bot_.py"]
