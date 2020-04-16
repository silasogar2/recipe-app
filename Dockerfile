FROM python:3.8-alpine
MAINTAINER Silas Ogar

ENV PYTHONUNBUFFERED 1

# intsall dependencies
copy ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# setting up directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app /app 

# creating a user 
RUN adduser -D user
RUN chown user:user -R /app/
USER user