FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000 5432

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]