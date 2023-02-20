import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge(executable_path=r'C:\Users\User\Desktop\msedge.exe')
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.XPATH,"//a[text()='Free Access to InterviewQues/ResumeAssistance/Material']").click()
time.sleep(3)

a = driver.window_handles
driver.switch_to.window(a[1])
time.sleep(4)
Var = driver.find_element(By.XPATH,"//a[text()='mentor@rahulshettyacademy.com']").text
driver.switch_to.window(a[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(Var)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("1234")

driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".alert")))
time.sleep(3)
print(driver.find_element(By.CSS_SELECTOR,".alert").text)




#V = driver.find_element(By.CSS_SELECTOR,".red").text
#var = V.split("at")[1].strip().split(" ")[0]
#print(var)