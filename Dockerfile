FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . .

