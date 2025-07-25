from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
time.sleep(1)

driver.find_element(By.CLASS_NAME, "btn-primary").click()

time.sleep(2)
driver.quit()
