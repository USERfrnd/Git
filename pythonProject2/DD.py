import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge(executable_path=r'C:\Users\User\Desktop\msedge.exe')
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,'autosuggest').send_keys('ind')
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='India']").click()


assert driver.find_element(By.ID,'autosuggest').get_attribute("value") == "India"
time.sleep(5)

driver.close()