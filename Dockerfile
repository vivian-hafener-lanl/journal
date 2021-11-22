FROM python:3.9.9-alpine
LABEL maintainer="Vivian Hafener"

RUN apk add tzdata && \
    cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
    echo "America/New_York" > /etc/timezone && \
    apk del tzdata

WORKDIR /app
RUN apk add build-base
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# ENTRYPOINT ["project/app.py"]
# CMD project/run.py
# CMD ["--bind=127.0.0.1:5000"]