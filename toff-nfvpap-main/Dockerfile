# syntax=docker/dockerfile:1
FROM python:3

ARG NODE_VERSION=16

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update \
    && apt-get install -y gnupg gosu curl ca-certificates zip unzip git \
    && curl -sLS https://deb.nodesource.com/setup_$NODE_VERSION.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm \
    && npm i flowbite \
    && apt-get -y autoremove 
COPY . /code/