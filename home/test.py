from django.test import TestCase
from rest_framework import status, response


class FirstTestCase(TestCase):
    def setUp(self):
        print("setup called")

    def test_equal(self):
        self.assertEqual(2, 2)
        response = self.client.get('/task2/')
        self.assertEqual(response.data, {'taskTitle': 'heo', 'taskDesc': 'df'})
