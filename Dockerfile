FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 4000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:4000"]
