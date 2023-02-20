import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Edge(executable_path=r'C:\Users\User\Desktop\msedge.exe')
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR,"#tinymce").clear()

driver.find_element(By.CSS_SELECTOR,"#tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
time.sleep(4)
