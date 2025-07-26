from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
time.sleep(1)

driver.find_element(
    By.XPATH, "//button[text()='Button with Dynamic ID']"
).click()


time.sleep(2)
driver.quit()
