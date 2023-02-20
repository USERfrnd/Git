import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('<path_to>/chromedriver ,options = chrome_options')
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
a = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
time.sleep(4)
result = len(a)
for i in a:
    product = i.find_element(By.XPATH,"div/h4/a").text
    if product == "Blackberry":
        i.find_element(By.XPATH,"div/button").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"a[class*='btn']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,".checkbox").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
b = driver.find_element(By.CSS_SELECTOR,".alert-success").text
assert "Success! Thank you!" in b