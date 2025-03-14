FROM python:3.12-alpine

WORKDIR /workspace

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .

CMD poetry run python s9/src/s9/bot.py