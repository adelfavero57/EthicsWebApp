from django.test import TestCase
from .models import Application
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
import time

# class RegisterTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):

#         cls.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

#         cls.application = Application.objects.create(user=cls.user, title="test", supervisor="alvin")

          

#     def testApplication(self):

#         item = Application.objects.get(user=self.user)
#         self.assertEqual(item, self.application)
#         # self.assertEqual(user.password, 'johnpassword')


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

    



