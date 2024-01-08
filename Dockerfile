FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt

COPY news /news
WORKDIR /news
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password news-user

USER news-user

