from django.test import TestCase
# Create your tests here.

class MyTests(TestCase):
    
    def test1(self):
        # Some test using self.foo
        response = self.client.post('login/', {'username': 'cpen2847', 'password': 'POL123@4'})

        self.assertEqual(response.status_code, 200)

