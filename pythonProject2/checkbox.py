import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge(executable_path=r'C:\Users\User\Desktop\msedge.exe')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
check = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(check))

for c in check:
    if c.get_attribute("value") == "option2":
        c.click()
        assert c.is_selected()
        break

time.sleep(5)

radio = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radio[0].click()
time.sleep(5)