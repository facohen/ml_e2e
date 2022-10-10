from locust import HttpUser, TaskSet, task, between, tag

"""
Run locus with:
locust -f ./tests/load_test.py
"""


class DiabetesPredict(TaskSet):
    @tag('Predictions')
    @task
    def predict(self):
        request_body = {"data": [[-0.00188202, -0.04464164, -0.05147406, -0.02632753, -0.00844872, -0.01916334,  0.07441156, -0.03949338, -0.06833155, -0.09220405]]}
        self.client.post('/v1/diabetes/predict', json=request_body)

    @tag('Baseline')
    @task
    def health_check(self):
        self.client.get('/')


class DiabetesLoadTest(HttpUser):
    tasks = [DiabetesPredict]
    host = 'http://127.0.0.1'
    stop_timeout = 200
    wait_time = between(1, 5)
