from selenium import webdriver
import time
import os

# Test to see if Last Modified button that can sort the application by Last Modified

# Get chrome driver
dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(10)

# Run the website on local machine in localhost, port 8000.
driver.get("http://localhost:8000/login/")
time.sleep(1)
driver.find_element_by_name("username").send_keys("zinc")
time.sleep(1)
driver.find_element_by_name("password").send_keys("12345678abc!")
time.sleep(1)
driver.find_element_by_name("Login").click()
time.sleep(1)
driver.find_element_by_name("Last Modified").click()
time.sleep(1)
driver.close()

