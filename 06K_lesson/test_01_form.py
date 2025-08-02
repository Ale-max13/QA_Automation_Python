from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_form_validation():
    service = Service(executable_path="drivers/msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    wait = WebDriverWait(driver, 10)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+798589998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    time.sleep(15)
    driver.quit()
