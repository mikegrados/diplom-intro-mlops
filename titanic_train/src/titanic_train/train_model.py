import sys
import joblib
import pandas as pd
import config
from titanic_utils.transformers import (
    MissingIndicator,
    CabinOnlyLetter,
    CategoricalImputerEncoder,
    NumericalImputesEncoder,
    RareLabelCategoricalEncoder,
    OneHotEncoder,
    MinMaxScaler,
    CleaningTransformer,
    DropTransformer,
)
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


numeric_transformer = Pipeline(
    steps=[
        ("missing_indicator", MissingIndicator(config.NUMERICAL_VARS)),
        ("median_imputation", NumericalImputesEncoder(config.NUMERICAL_VARS)),
    ]
)

categorical_transformer = Pipeline(
    steps=[
        ("cabin_only_letter", CabinOnlyLetter("cabin")),
        (
            "categorical_imputer",
            CategoricalImputerEncoder(
                config.CATEGORICAL_VARS
            ),
        ),
        (
            "rare_labels",
            RareLabelCategoricalEncoder(
                tol=0.02, variables=config.CATEGORICAL_VARS
            ),
        ),
        ("one_hot", OneHotEncoder(config.CATEGORICAL_VARS)),
    ]
)

preprocessor = Pipeline(
    [
        ("cleaning", CleaningTransformer()),
        ("categorical", categorical_transformer),
        ("numeric", numeric_transformer),
        ("dropper", DropTransformer(config.DROP_COLS)),
        ("scaling", MinMaxScaler()),
    ]
)


def train(model_name: str):

    if model_name == 'RandomForest':
        regressor = RandomForestClassifier(
            max_depth=4, class_weight="balanced",
            random_state=config.SEED_MODEL
        )

    else:
        regressor = LogisticRegression(
            C=0.0005, class_weight="balanced",
            random_state=config.SEED_MODEL
        )

    titanic_pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
            (f"{model_name}_regressor", regressor),
        ]
    )

    df = pd.read_csv(config.URL).drop(columns="home.dest")

    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(config.TARGET, axis=1),
        df[config.TARGET],
        test_size=config.TEST_SIZE,
        random_state=config.SEED_SPLIT,
    )

    titanic_pipeline.fit(X_train, y_train)

    preds = titanic_pipeline.predict(X_test)
    accuracy = (preds == y_test).sum() / len(y_test)
    print(f"Accuracy of the {model_name} model is {accuracy}")

    print(f"Model stored in {config.MODEL_NAME}")
    joblib.dump(titanic_pipeline, f"{config.MODEL_NAME}")


if __name__ == "__main__":
    model = str(sys.argv[1]) if len(sys.argv) > 1 else 'LogisticRegression'
    train(model_name=model)
