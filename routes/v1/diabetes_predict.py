from fastapi import APIRouter
from models.schemas.diabetes import Diabetes, DiabetesPredictionResponse
import models.ml.classifier as clf

app_diabetes_predict_v1 = APIRouter()


@app_diabetes_predict_v1.post('/diabetes/predict',
                          tags=["Predictions"],
                          response_model=DiabetesPredictionResponse,
                          description="Get a prediction from Diabetes")
async def get_prediction(diabetes: Diabetes):
    data = dict(diabetes)['data']
    prediction = clf.model.predict(data).tolist()
    return {"prediction": prediction}

