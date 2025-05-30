FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /expense_tracker
 
COPY requirements.txt /expense_tracker/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /expense_tracker/


























