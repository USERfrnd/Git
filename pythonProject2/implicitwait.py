import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge(executable_path=r'C:\Users\User\Desktop\msedge.exe')
driver.implicitly_wait(8)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
driver.find_element(By.XPATH,"//button[text()='ADD TO CART']").click()

#cart = len(a)


#for result in a:
   # result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)


