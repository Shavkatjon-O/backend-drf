FROM python:3.12-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gettext \
    postgresql-client \
    netcat \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/base.txt requirements/base.txt
COPY requirements/production.txt requirements/production.txt

RUN pip install --upgrade pip && pip install -r requirements/production.txt

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

RUN mkdir -p $HOME

RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/locales
RUN mkdir $APP_HOME/media

WORKDIR $APP_HOME

COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

RUN rm -rf /var/cache/apt/*
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN rm -rf /etc/apk/cache
