import models.ml.classifier as clf
from fastapi import FastAPI
from joblib import load
from routes.v1.diabetes_predict import app_diabetes_predict_v1
from routes.home import app_home


app = FastAPI(title="Diabetes ML API", description="API for diabetes dataset ml model", version="1.0")


@app.on_event('startup')
async def load_model():
    clf.model = load('models/ml/diabetes_v1.joblib')


app.include_router(app_home)
app.include_router(app_diabetes_predict_v1, prefix='/v1')

