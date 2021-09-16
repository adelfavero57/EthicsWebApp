from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
# Create your tests here.

class Story1(TestCase):
    
    def test1(self):
        # test if someone can type username and password 
        response = self.client.post('/login/', {'username': 'cpen2847', 'password': 'POL123@4'})
        self.assertEqual(response.status_code, 200)

    
    def test2(self):
        # test if the page redirct to the managelist page when user login in successfully
        
        pass


    def test3(self):
        # If a user is already logged in they should be automatically redirected to the managelist page

        pass

    def test4(self):
        # A user inputs incorrect details and a response is displayed on the login page indicating the error

        pass



class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path = '/Users/alvinpeng/Desktop/chromedriver')
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):

        
        # test if someone can  login the page
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('cpen2847')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('POL123@4')
        self.selenium.find_element_by_xpath('//*[@id="login"]').click()

    



