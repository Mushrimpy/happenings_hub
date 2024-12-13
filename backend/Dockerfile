FROM python:3.10

WORKDIR /app/

ENV PYTHONPATH=/app

COPY ./app /app/app

CMD ["fastapi", "run", "app/main.py"]
