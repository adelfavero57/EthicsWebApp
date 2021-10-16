from django.test import TestCase, RequestFactory
from django.test import Client
from accounts.forms import CreateUserForm
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.models import Group
from accounts.views import registerPage, editUserPage, loginPage
from django.contrib.sessions.middleware import SessionMiddleware
# from django.test import LiveServerTestCase
# from selenium.webdriver.chrome.webdriver import WebDriver
# import time


class AccountsTest(TestCase):

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

        
          

    def testNoEmail(self):

        data = {'first_name': 'Test', 'last_name': 'Test', 'username': "Test", 'password1': 'admin', 'password2': 'admin'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")

    def testNoFirstName(self):

        data = {'last_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com', 'password1': 'admin', 'password2': 'admin'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")


    def testNoLastName(self):

        data = {'first_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com', 'password1': 'admin', 'password2': 'admin'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")

    
    def testWrongPasswordFormat(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com', 'password1': 'admin', 'password2': 'admin'}

        form = CreateUserForm(data)

        self.assertFalse(form.is_valid(), "The test did not pass")


    def testCorrectPasswordFormat(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        form = CreateUserForm(data)

        self.assertTrue(form.is_valid(), "The test did not pass")

    
    def test_registerPage1(self):

        data = {'first_name': 'Test','last_name': 'Test', 'username': "Test", 'email': 'hello@gmail.com', 'password1': 'POL123@4', 'password2': 'POL123@4'}

        request = self.factory.post('/register/', data, follow=True)

        request.user = AnonymousUser()

        response = registerPage(request)

        self.assertEqual(response.headers['Location'], '/login/')
        self.assertEqual(response.status_code, 302)

    def test_registerPage2(self):

        request = self.factory.get('/register/')

        request.user = AnonymousUser()

        response = registerPage(request)

        

    
    def test_editUserPage1(self):

        data = {'first_name': 'change','last_name': 'change', 'username': "change", 'email': 'change@gmail.com'}


        request = self.factory.post('/edit_profile/', data, follow = True)


        request.user = self.user

        response = editUserPage(request)

        self.assertEqual(response.status_code, 302)


    
    def test_editUserPage2(self):

        request = self.factory.get('/edit_profile/')

        request.user = self.user

        response = editUserPage(request)

        self.assertEqual(response.status_code, 200)



    def test_login1(self):
        

        data = {'username': "admin", 'password': 'adminpassword', 'remember_me': False}

        request = self.factory.post('/login/', data)

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        

        request.user = AnonymousUser()

        response = loginPage(request)

        self.assertEqual(response.headers['Location'], '/approvelist/')
        self.assertEqual(response.status_code, 302)


    def test_login2(self):

        data = {'username': "john", 'password': 'johnpassword', 'remember_me': False}

        request = self.factory.post('/login/', data)

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        request.user = AnonymousUser()

        response = loginPage(request)

        self.assertEqual(response.headers['Location'], '/managelist/')
        self.assertEqual(response.status_code, 302)

    
    def test_login3(self):

        other = User.objects.create_user(username = 'test', password='testpassword')

        data = {'username': "test", 'password': 'testpassword', 'remember_me': False}

        request = self.factory.post('/login/', data)

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = AnonymousUser()
        response = loginPage(request)

        #self.assertEqual(response.headers['Location'], '/login/')
        self.assertEqual(response.status_code, 200)


    def test_login4(self):

        request = self.factory.get('/login')
        request.user = AnonymousUser()
        response = loginPage(request)
        
        self.assertEqual(response.status_code, 200)










        





    

























        # response = self.
        
        # self.assertFormError(response, 'form', 'username', 'username must be 150 characters or fewer, must contain letters, digits and @/./+/-/_ only')

#     def testAnswer(self):
#         pass


#     def testQuestion(self):
#         pass


# class SimpleTest(TestCase):
    
    
#     def test_register(self):
#         response = self.client.get('/register/')
#         self.assertEqual(response.status_code, 200)





# class MySeleniumTests(LiveServerTestCase):

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#         group = Group.objects.
#         cls.selenium = WebDriver(executable_path = '/Users/alvinpeng/Desktop/chromedriver')
#         cls.selenium.implicitly_wait(10)



#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()

#     def test_login(self):

#         time.sleep(3)
#         # test if someone can  login the page
#         self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
#         username_input = self.selenium.find_element_by_name("username")
#         username_input.send_keys('admin')
#         time.sleep(3)
#         password_input = self.selenium.find_element_by_name("password")
#         password_input.send_keys('admin')
#         time.sleep(3)
#         self.selenium.find_element_by_xpath('//*[@id="login"]').click()
#         time.sleep(3)

    



