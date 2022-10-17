import os

URL = "https://www.openml.org/data/get_csv/16826755/phpMYEkMl"
BASE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
ROOT_DIR = os.path.realpath(os.path.join(BASE_DIR, ".."))
MODEL_NAME = os.path.realpath(os.path.join(ROOT_DIR, "models", "model.sav"))

SEED_SPLIT = 404
SEED_MODEL = 404
TEST_SIZE = 0.2

TARGET = "survived"
FEATURES = [
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "cabin",
    "embarked",
    "title",
]

NUMERICAL_VARS = ["pclass", "age", "sibsp", "parch", "fare"]
CATEGORICAL_VARS = ["sex", "cabin", "embarked", "title"]
DROP_COLS = ["boat", "body", "ticket", "name"]
