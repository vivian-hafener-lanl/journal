FROM python:3.9.7
MAINTAINER Vivian Hafener
ADD . /journal
WORKDIR /journal
RUN pip install -r requirements.txt
CMD "project/main.py"