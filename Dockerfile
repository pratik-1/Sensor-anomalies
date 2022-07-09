FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /app

WORKDIR /app


COPY . /app/

RUN pip install --upgrade pip
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps


#RUN black *.py
#RUN pylint --disable=R,C *.py
#RUN pytest -v --cov-report term-missing --cov=. anomalies/tests/test_count_anomalies.py

#Uncomment to run format, lint and test
# RUN make all

