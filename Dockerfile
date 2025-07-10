
FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /expense_tracker


COPY requirements.txt .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

















