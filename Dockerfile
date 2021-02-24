FROM ubuntu:latest
WORKDIR /app

RUN apt-get update -y && apt-get upgrade -y
# For some reason it needs --fix-missing, seriously apt...
RUN apt-get update --fix-missing
RUN apt-get install -y python3 python3-pip

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD cd /app/holo_schedule_api && FLASK_APP=server.py flask run