from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
import json
import time


STUDENT_EMAIL = "kdo55%40uw.edu"
WEB_ADDRESS = f"https://edstem.org/us/courses/50191/lessons/87193/attempts?email={STUDENT_EMAIL}&slide=486954" # for stonks
STAFF_EMAIL = "rlin0622@uw.edu"
STAFF_PASSWORD = "XXXX"
TIME_OUT = 60

driver = webdriver.Safari() # change this if u dont use safari
driver.get(WEB_ADDRESS)

# ed login

login = WebDriverWait(driver, TIME_OUT).until(lambda x: x.find_element(By.XPATH, '//*[@id="x1"]'))
login.send_keys(STAFF_EMAIL, Keys.ENTER)

# uw NETid redirect
login = WebDriverWait(driver, TIME_OUT).until(lambda x: x.find_element(By.XPATH, '//*[@id="weblogin_netid"]'))
login.send_keys(STAFF_EMAIL.split('@')[0], Keys.ENTER)

time.sleep(1)
login = WebDriverWait(driver, TIME_OUT).until(lambda x: x.find_element(By.XPATH, '//*[@id="weblogin_password"]'))
login.send_keys(STAFF_PASSWORD, Keys.ENTER)

# make sure you accept duo mobile
time.sleep(30)

# pressing "this is my device button"
WebDriverWait(driver, TIME_OUT).until(lambda x: x.find_element(By.XPATH, '//*[@id="trust-browser-button"]').click())

# ed scraiping
student_code = WebDriverWait(driver, TIME_OUT * 100 ).until(lambda x: x.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/main/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div[3]/div/div[4]/div/div[2]/div/div/div[1]/div/div/table"))
print(student_code)

student_feedback = WebDriverWait(driver, TIME_OUT * 100).until(lambda x: x.find_elements(By.CLASS_NAME, "amber-el amber-paragraph amber-content"))

