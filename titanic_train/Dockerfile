ARG PYTHON_VERSION=3.9

FROM python:${PYTHON_VERSION}
COPY requirements.txt ./
COPY src ./src
RUN mkdir models \
    && pip install -r ./requirements.txt \
    && python ./src/titanic_train/train_model.py
