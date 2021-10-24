from django.test import TestCase, RequestFactory
from django.test import Client
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.models import Group
from coversheet.views import coversheetPage
from accounts.models import Application



# Create your tests here.


class CoversheetTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        researcher = Group(name = "researcher")
        staff = Group(name = "staff")
        staff.save()
        researcher.save()
        cls.user = User.objects.create_user(username = 'john', password='johnpassword')
        cls.admin_staff = User.objects.create_user(username='admin', password='adminpassword')
        cls.admin_staff.groups.add(staff)
        cls.user.groups.add(researcher)
        cls.factory = RequestFactory()

    
    def test_coversheet(self):

        new_application = Application.objects.create(id = 1, user=self.user, status = "IN PROGRESS", supervisor="Alvin", title="Test")

        data = {'summary': 'test', "protocol": "test", "investigatorname": "Alvin",
         'investigatorid': "1", 'center': '1', 'role': 'chiefinvestigator',
         'otherinternalinvestigators': 'No', 'internalinvestigatorsnumber': '1',
         'otherexternalinvestigators': 'No', 'externalinvestigatorsnumber': '1',
         'responsible': '1', 'currentstate': '1', 'HRECname': '1', 
         'action': '1', 'title': '1', 'contractaction': '1', 'otherrelevantdetails': '1'}

        request = self.factory.post('/coversheet/1', data)

        request.user = self.user
        response = coversheetPage(request, 1)

        print(response)

