FROM python:3.10-bullseye
LABEL authors="SiGae@protonmail.com"

COPY . .
ENV POETRY_VERSION=1.4.2 POETRY_HOME=/poetry
ENV PATH=/poetry/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry install --no-root

CMD poetry run python main.py