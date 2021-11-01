from selenium import webdriver
import time
import os

# Test to see if sign up hyperlink redirects to register page

# Get chrome driver
dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(10)

# Run the website on local machine in localhost, port 8000.
driver.get("http://localhost:8000/login/")
time.sleep(5)
driver.find_element_by_name("username").send_keys("normaluser")
time.sleep(5)
driver.find_element_by_name("password").send_keys("qwer1234zxcv")
time.sleep(5)
driver.find_element_by_name("Login").click()
time.sleep(5)
driver.find_element_by_name("start").click()
time.sleep(5)
driver.get("http://localhost:8000/qualifier/success/")
time.sleep(5)
driver.find_element_by_name("next").click()
time.sleep(5)
driver.find_element_by_name("summary").send_keys("summary for virtual test")
time.sleep(5)
driver.find_element_by_name("protocol").send_keys("protocol for virtual test")
time.sleep(5)
driver.find_element_by_name("investigatorname").send_keys("investigator name for virtual test")
time.sleep(5)
driver.find_element_by_name("investigatorid").send_keys("investigator id for virtual test")
time.sleep(5)
driver.find_element_by_name("center").send_keys("school / centre for virtual test")
time.sleep(5)
driver.find_element_by_name("role").send_keys("chief investigator")
time.sleep(5)
driver.find_element_by_name("Logout").click()
time.sleep(5)
driver.close()