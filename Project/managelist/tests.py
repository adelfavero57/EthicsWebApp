from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from accounts.models import Application

# Create your tests here.

class ManagelistTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        researcher = Group(name = "researcher")
        researcher.save()
        cls.user = User.objects.create_user(username = 'john', password='johnpassword')
        cls.user.groups.add(researcher)
    
    

    def test_no_login(self):

        # you can not directly access the managelist page

        response = self.client.get('/managelist/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        c = Client()

        response = c.post('/login/', {'username': 'john', 'password': 'johnpassword'}, follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.redirect_chain[0][0], '/managelist/', "The page did not redirct to the managelist page")
        self.assertEqual(response.redirect_chain[0][1], 302, "The page did not redirct to the managelist page")

        
    def test_application(self):

    
        new_application = Application.objects.create(id = 1, user=self.user, status = "IN PROGRESS", supervisor="Alvin", title="Test")
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'johnpassword'}, follow=True)

        

        applications = response.context['applications']

        instance = applications.get(pk=1)

        self.assertEqual(instance.status, "IN PROGRESS")
        self.assertEqual(instance.title, "Test")
        self.assertEqual(instance.supervisor, "Alvin")

        




        
        






        

    

