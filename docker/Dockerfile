FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
RUN pip install poetry
COPY pyproject.toml poetry.lock /usr/src/app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction


COPY . /usr/src/app

CMD ["gunicorn app.asgi:application -b 0.0.0.0:8000 --reload"]