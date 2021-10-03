from selenium import webdriver
import time
import os

# Test to see if login is working and identify different user. 

# Get chrome driver
dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(10)

# Run the website on local machine in localhost, port 8000.
driver.get("http://localhost:8000/login/")
time.sleep(5)
driver.find_element_by_name("username").send_keys("zinc")
time.sleep(5)
driver.find_element_by_name("password").send_keys("zinc")
time.sleep(5)
driver.find_element_by_name("Login").click()
time.sleep(5)

# Test to see if the normal user can go to adminpage
driver.get("http://localhost:8000/approvelist/")
time.sleep(5)
driver.close()