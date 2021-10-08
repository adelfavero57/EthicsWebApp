from django.test import TestCase
from django.test import Client

# Create your tests here.

class ManagelistTest(TestCase):

    def test_no_application(self):

        response = self.client.get('managelist')
        self.assertEqual(response.status_code, 200)
