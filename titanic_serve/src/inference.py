import sys
import json
import joblib
import config
import pandas as pd
from sklearn.pipeline import Pipeline
from fastapi import FastAPI, Depends


class TitanicModel:

    prod_model: Pipeline

    def load_model(self):
        """Loads the model"""
        self.prod_model = joblib.load(config.MODEL_NAME)
        self.name = self.prod_model.get_params()['steps'][1][0]

    def predict(self, input: config.PredictionInput) -> config.PredictionOutput:
        """Runs a prediction"""
        df = pd.DataFrame([input.dict()])
        if not self.prod_model:
            raise RuntimeError("Model is not loaded")
        prediction = self.prod_model.predict(df)[0]
        # results = {"input_raw": input.dict(), "prediction": str(prediction),
        #            "model": self.name}
        return config.PredictionOutput(prediction=prediction, model=self.name)


app = FastAPI()
titanic_model = TitanicModel()

@app.post("/inference")
async def inference(
    output: config.PredictionOutput = Depends(titanic_model.predict),
) -> config.PredictionOutput:
    return output

@app.post("/")
async def root():
    return "Hello World"

@app.on_event("startup")
async def startup():
    titanic_model.load_model()
