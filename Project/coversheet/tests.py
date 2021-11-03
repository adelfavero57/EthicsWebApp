from django.test import TestCase, RequestFactory
from django.test import Client
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.models import Group
from coversheet.views import coversheetPage
from accounts.models import Application
from accounts.models import CoverSheetQuestion, CoverSheetAnswers



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

        CoverSheetQuestion.objects.bulk_create([

            CoverSheetQuestion(question_num=1001, text = 'Provide a lay summary of the project:', is_short_answer=1),
            CoverSheetQuestion(question_num=1002, text = 'Protocol Title:', is_short_answer=1),
            CoverSheetQuestion(question_num=1003, text = 'First Named Chief Investigator Name:', is_short_answer=1),
            CoverSheetQuestion(question_num=1004, text = 'First Named Chief Investigator ID:', is_short_answer=1),
            CoverSheetQuestion(question_num=1005, text = 'School/Centre', is_short_answer=0),
            CoverSheetQuestion(question_num=1006, text = 'Role', is_short_answer=1),
            CoverSheetQuestion(question_num=1007, text = 'Other Internal Investigators Involved:', is_short_answer=0),
            CoverSheetQuestion(question_num=1008, text = 'Number of Internal Investigators (including Chief Investigator):', is_short_answer=0),
            CoverSheetQuestion(question_num=1009, text = 'Other External Investigators Involved:', is_short_answer=0),
            CoverSheetQuestion(question_num=1010, text = 'Number of External Investigators:', is_short_answer=0),
            CoverSheetQuestion(question_num=1011, text = 'Responsible:', is_short_answer=1),
            CoverSheetQuestion(question_num=1012, text = 'Current State:', is_short_answer=1),
            CoverSheetQuestion(question_num=1013, text = 'HREC name:', is_short_answer=1),
            CoverSheetQuestion(question_num=1014, text = 'Action:', is_short_answer=1),
            CoverSheetQuestion(question_num=1015, text = 'Title:', is_short_answer=1),
            CoverSheetQuestion(question_num=1016, text = 'Action:', is_short_answer=1),
            CoverSheetQuestion(question_num=1017, text = 'Please provide any other relevant details:', is_short_answer=1),
        ])

        CoverSheetAnswers.objects.bulk_create([

            CoverSheetAnswers(question_id = 1001, is_short_answer = 1)
        ])





    
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

