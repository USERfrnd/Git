import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions (link for chrome options)
driver = webdriver.Chrome('<path_to>/chromedriver ,options = chrome_options')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action= ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).perform()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
