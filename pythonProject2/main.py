

from selenium import webdriver


#driver = webdriver.Chrome(r'Path_to_chrome_Driver\\chromedriver.exe')
#driver = webdriver.Chrome('<path_to>/chromedriver')
#driver = webdriver.Firefox(executable_path=r'C:\Users\User\Desktop\gecko.exe')
driver = webdriver.Edge(executable_path=r'C:\Users\User\Desktop\msedge.exe')
driver.maximize_window()
driver.get("https:/rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://www.rahulshettyacademy.com/#/practice-project")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
