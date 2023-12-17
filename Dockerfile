# Используем базовый образ Python
FROM python:3.11


# Устанавливаем рабочую директорию в контейнере
WORKDIR /futuresproject

# Копируем файлы зависимостей в контейнер
COPY requirements.txt requirements.txt

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы из текущего каталога в контейнер
COPY . .

# Определяем команду для запуска Django приложения внутри контейнера
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
