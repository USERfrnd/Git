from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximised")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
#https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions (link for chrome options)
driver = webdriver.Chrome('<path_to>/chromedriver ,options = chrome_options')

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)