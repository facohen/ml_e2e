from pydantic import BaseModel, conlist
from typing import List, Any

class Diabetes(BaseModel):
    data: List[conlist(float, min_items=10, max_items=10)]

class DiabetesPredictionResponse(BaseModel):
    prediction: List[int]
