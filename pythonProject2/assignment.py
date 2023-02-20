import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge(executable_path=r'C:\Users\User\Desktop\msedge.exe')

expectedlist = ['Cucumber - 1 Kg' , 'Raspberry - 1/4 Kg' , 'Strawberry - 1/4 Kg']

Actuallist = []

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(8)
a = driver.find_elements(By.XPATH,"//div[@class='products']/div")
time.sleep(5)
result = len(a)
for i in a:
    Actuallist.append(i.find_element(By.XPATH,"h4").text)
    i.find_element(By.XPATH,"div/button").click()

assert expectedlist == Actuallist
print(Actuallist)

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

time.sleep(4)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

a = WebDriverWait(driver,10)
a.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")

sum=0
for price in prices:
    sum = sum +int(price.text)

print(sum)
Total = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == Total

discountamt = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert Total > discountamt
