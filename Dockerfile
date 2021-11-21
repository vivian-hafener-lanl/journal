FROM python:3.9.9-alpine
LABEL maintainer="Vivian Hafener"

RUN apk add tzdata && \
    cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
    echo "America/New_York" > /etc/timezone && \
    apk del tzdata

WORKDIR /project
RUN apk add build-base
ADD requirements.txt /project
RUN pip3 install -r requirements.txt
ADD . /project

ENTRYPOINT ["python3"]
CMD project/run.py
# CMD ["--bind=127.0.0.1:5000"]