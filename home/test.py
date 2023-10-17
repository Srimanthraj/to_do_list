from django.test import TestCase
from rest_framework import status, response


class FirstTestCase(TestCase):
    def setUp(self):
        print("setup called")

    def test_equal(self):
        response = self.client.get('/tasks2/')
        self.assertEqual(response.data, {'taskDesc': 'df', 'taskTitle': 'heo'})
        self.assertEqual(1, 1)
