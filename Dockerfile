# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /todo

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
