FROM python:3.10.8

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /usr/src/app/

RUN poetry install --only main

COPY . /usr/src/app/