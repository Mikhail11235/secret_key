FROM python:3.9-slim

WORKDIR /app

ENV NOT_LOCAL=1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]