from fastapi.testclient import TestClient
from app import app


def test_success_prediction():
    endpoint = '/v1/diabetes/predict'
    body = {"data": [[-0.00188202, -0.04464164, -0.05147406, -0.02632753, -0.00844872, -0.01916334,  0.07441156, -0.03949338, -0.06833155, -0.09220405]]}

    with TestClient(app) as client:
        response = client.post(endpoint, json=body)
        response_json = response.json()
        assert response.status_code == 200
        assert 'prediction' in response_json


def test_bad_request():
    endpoint = '/v1/diabetes/predict'
    body = {"data": [[-0.00188202, -0.04464164, -0.05147406, -0.02632753, -0.00844872, -0.01916334,  0.07441156, -0.03949338, -0.06833155, -0.09220405]]}

    with TestClient(app) as client:
        response = client.post(endpoint, json=body)
        assert response.status_code == 422
