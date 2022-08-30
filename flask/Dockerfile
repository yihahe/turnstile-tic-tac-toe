# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

ADD . /code
WORKDIR /code

EXPOSE 5000

RUN pip3 install -r requirements.txt

CMD [ "python3" , "flask_home.py", "runserver", "0.0.0.0:5000"]