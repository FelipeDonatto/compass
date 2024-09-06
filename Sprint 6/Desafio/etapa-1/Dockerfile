FROM python:3

WORKDIR /usr/src/app

VOLUME /usr/src/app/dados

COPY ./dados /usr/src/app/dados
COPY ./script.py /usr/src/app/script.py


ENV AWS_ACCESS_KEY_ID="xxxx"
ENV AWS_SECRET_ACCESS_KEY="xxxxx"
ENV AWS_SESSION_TOKEN="xxxxx"

RUN pip install boto3

CMD ["python", "./script.py" ]