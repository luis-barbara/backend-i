FROM python:3.12-slim

WORKDIR /workspace

RUN pip install poetry

COPY . .

RUN poetry install -nq

ENTRYPOINT [ "poetry", "run", "uvicorn"]

CMD [ "s12.main:api", "--host", "0.0.0.0"]



