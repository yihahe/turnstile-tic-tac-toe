# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /flask
COPY app ./app/
COPY flask .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD [ "python3" , "flask_home.py"]