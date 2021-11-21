FROM python:3.9.7
MAINTAINER Vivian Hafener

# RUN apk add tzdata && \
#     cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
#     echo "America/New_York" > /etc/timezone && \
#     apk del tzdata

WORKDIR /project
ADD requirements.txt /project
RUN pip install -r requirements.txt
ADD . /project

ENTRYPOINT ["python3"]
CMD python3 project/run.py
# CMD ["--bind=127.0.0.1:5000"]