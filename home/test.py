from django.test import TestCase
from rest_framework import status

from .models import Task


class FirstTestCase(TestCase):
    def setUp(self):
        Task.objects.create(taskTitle='ho', taskDesc='df')

    def test_api_response(self):
        api_response = self.client.get('/task3/')
        task = Task.objects.get(taskTitle='heo', taskDesc='df')
        print("got")
        self.assertEqual(api_response.data, {
                         'taskTitle': task.taskTitle, 'taskDesc': task.taskDesc})
