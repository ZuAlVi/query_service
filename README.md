# 🗺 Query Service

[![Python Version](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django Version](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![DRF Version](https://img.shields.io/badge/DRF-3.15-524E20.svg)](https://www.djangoproject.com/)
[![DRF YASG Version](https://img.shields.io/badge/DRF_YASG-1.21-333E20.svg)](https://www.djangoproject.com/)
[![PostgreSQL Version](https://img.shields.io/badge/PostgreSQL-16.0-088E20.svg)](https://www.postgresql.org/)
[![Docker Version](https://img.shields.io/badge/Docker-26.0-942E20.svg)](https://www.docker.com/)
[![Docker Compose Version](https://img.shields.io/badge/Docker_Compose-2.26-521E20.svg)](https://www.docker.com/)

Этот проект представляет собой реализацию сервиса на Django REST Framework (DRF) для обработки запросов, отправки их на внешний сервер и хранения истории запросов и ответов.

## Возможности

- 📡 Отправка запросов с кадастровым номером, широтой и долготой
- ⏱ Эмуляция отправки запроса на внешний сервер с задержкой до 60 секунд
- 🔄 Генерация случайного ответа (true или false)
- 📂 Хранение истории запросов и ответов в базе данных
- 📑 Получение списка всех запросов
- 📜 Получение списка запросов по кадастровому номеру
- 🏓 Проверка работоспособности сервера через эндпоинт /ping

## 💽 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/ZuAlVi/query_service.git
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv env

source env/bin/activate  # для Windows: env\Scripts\activate
```
3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Создайте в корне проекта файл .env и заполните его необходимыми данными взяв за пример файл .env_example


5. Создайте базу данных.


6. Примените миграции для создания таблиц в базе данных:

```bash
python manage.py migrate
```

7. Создайте суперпользователя для административного интерфейса Django:

```bash
python manage.py createsuperuser
```
## 🚀 Запуск

1. Запустите сервер Django:
```bash
python manage.py runserver
```
Дополнительный сервис для эмуляции внешнего сервера будет запущен автоматически.

## 🔚 Эндпоинты

- POST /query/: отправить запрос с кадастровым номером, широтой и долготой
- POST /result/: обновить ответ для соответствующего запроса
- GET /history/: получить список всех запросов
- GET /history/<cadastral_number>/: получить список запросов по кадастровому номеру
- GET /ping/: проверить работоспособность сервера

## 👮‍♂️ Административный интерфейс

Для доступа к административному интерфейсу Django перейдите по адресу http://localhost:8000/admin/ и авторизуйтесь с помощью созданного суперпользователя.

## 📖 Документация

Для динамического создания документации API к проекту подключен SWAGGER и REDOC.

Для просмотра документации нужно перейти по адресу:
```bash
http://localhost:8000/swagger/
```
или
```bash
http://localhost:8000/redoc/
```

## ✅ Тесты

- Для запуска тестов:

```bash
python manage.py test
```

- Посмотреть процент покрытия тестами:

```bash
coverage run --source='.' manage.py test

coverage report
```

## 🐳 Запуск через Docker и Docker Compose

1. Docker:
    
- Создаем контейнер:

```bash
docker build -t app-name .
 ```

- Запускаем:

```bash
docker run -p 8000:8000 app-name
 ```

2. Docker Compose:

- Собираем и запускаем контейнер в фоновом режиме одной командой:

```bash
docker-compose up --build
 ```

После этого сервис будет доступен по адресу http://localhost:8000/.
