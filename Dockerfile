FROM python:3.11-alpine3.16

COPY requirements.txt /temp/requirements.txt

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

COPY candidates /candidates
WORKDIR /candidates
EXPOSE 8000

RUN adduser --disabled-password service-user

USER service-user
