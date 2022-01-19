FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10

RUN mkdir app
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY src .