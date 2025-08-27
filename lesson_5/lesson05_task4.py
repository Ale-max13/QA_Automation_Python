from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

message = driver.find_element(By.ID, "flash")
print(message.text.strip())

time.sleep(2)
driver.quit() 

# Альтернатива без переменной:
# driver.find_element(By.ID, "username").send_keys("tomsmith")
