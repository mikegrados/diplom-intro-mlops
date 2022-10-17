ARG PYTHON_VERSION=3.9

FROM python:${PYTHON_VERSION}
COPY poetry.lock ./
COPY pyproject.toml ./
COPY src ./src
RUN mkdir models \
    && pip install poetry \
    && poetry install \
    && python src/titanic_train/train_model.py
