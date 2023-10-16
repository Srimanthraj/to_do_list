from rest_framework import status
from rest_framework.test import APIClient


class TestCreateTask:
    def test_if_task_created(self):
        client = APIClient()
        response = client.post('/')
