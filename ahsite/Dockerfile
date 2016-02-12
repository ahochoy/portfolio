FROM python:2.7
MAINTAINER Andrew HoChoy <a.hochoy@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install ruby libpcre3 -y
RUN gem install sass

RUN mkdir /usr/src/www
WORKDIR /usr/src/www

ADD ./requirements.txt ./
RUN pip install -r requirements.txt

ADD ./ ./
