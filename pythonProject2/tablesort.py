from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
BrowserSortedList=[]

driver = webdriver.Chrome('<path_to>/chromedriver ,options = chrome_options')
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on column header

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

#collect all veggie names -> browsersorted veggielist(A,B,C)

VeggieElements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in VeggieElements:
    BrowserSortedList.append (ele.text)

Originallist = BrowserSortedList.copy()

#sort this BrowserSortedVeggies -> newSortedlist(A,B,C)

BrowserSortedList.sort()

assert BrowserSortedList == Originallist