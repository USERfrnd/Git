import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name="Salona"
driver = webdriver.Edge(executable_path=r'C:\Users\User\Desktop\msedge.exe')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
a = driver.switch_to.alert
alert = a.text
print(alert)
assert name in alert
a.accept()
a.dismiss()





