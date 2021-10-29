FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

ARG MODE

COPY ./django/ /app/
COPY docker/build.sh /app/
COPY docker/requirements/. /app/
COPY docker/entrypoint.sh /

RUN sh build.sh

ENTRYPOINT ["/entrypoint.sh"]
