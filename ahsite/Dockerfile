FROM python:2.7
MAINTAINER Andrew HoChoy <a.hochoy@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install ruby libpcre3 -y
RUN gem install sass

COPY S3.py /usr/local/lib/python2.7/site-packages

RUN mkdir /usr/src/www
WORKDIR /usr/src/www

ADD ./requirements.txt ./
RUN pip install -r requirements.txt --upgrade

ADD ./ ./
