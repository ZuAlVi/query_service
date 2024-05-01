FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . .

# Команда для запуска приложения при старте контейнера
#CMD ["python", "manage.py", "runserver"]

