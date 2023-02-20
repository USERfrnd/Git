import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Edge(executable_path=r'C:\Users\User\Desktop\msedge.exe')
driver.implicitly_wait(15)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
window = driver.window_handles
driver.switch_to.window(window[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
time.sleep(3)
driver.close()
driver.switch_to.window(window[0])
assert "Opening a new window"== driver.find_element(By.TAG_NAME,"h3").text





