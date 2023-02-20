import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('<path_to>/chromedriver')

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME,"name").send_keys("SALONA")
driver.find_element(By.NAME,"email").send_keys("salonanizam@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("45678")
driver.find_element(By.ID,"exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rahul")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message= driver.find_element(By.CLASS_NAME,'alert-success').text
print(message)
assert "success" in message

#driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
driver.find_element(By.CSS_SELECTOR,'#inlineRadio1')
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("helloagain")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

#static dropdown

dropdown = Select (driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
time.sleep(2)
#dropdown.select_by_value()

driver.close()