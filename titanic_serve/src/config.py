import os
from pydantic import BaseModel

BASE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
ROOT_DIR = os.path.realpath(os.path.join(BASE_DIR, ".."))

MODEL_NAME = os.path.realpath(os.path.join(ROOT_DIR, "titanic_train\\models", "model.sav"))
LOG_DIR = os.path.realpath(os.path.join(ROOT_DIR, "titanic_serve\\logs"))

class PredictionInput(BaseModel):
    pclass: int
    name: str
    sex: str
    age: str
    sibsp: int
    parch: int
    ticket: str
    fare: str
    cabin: str
    embarked: str
    boat: str
    body: str


class PredictionOutput(BaseModel):
    prediction: int
    model: str