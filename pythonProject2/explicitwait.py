import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge(executable_path=r'C:\Users\User\Desktop\msedge.exe')
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("berr")
time.sleep(3)
#(for one item)
driver.find_element(By.XPATH,"//button[text()='ADD TO CART']").click()


driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
a = WebDriverWait(driver,10)
a.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

#sum validation(for one item)
driver.find_elements(By.CSS_SELECTOR,"tr td p")
sum = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

print(sum)
