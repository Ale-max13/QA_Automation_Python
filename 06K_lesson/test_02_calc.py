from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_calc_slow():
    service = Service(executable_path=os.path.abspath("lesson_5/geckodriver.exe"))
    driver = webdriver.Firefox(service=service)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    try:
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        result = driver.find_element(By.CLASS_NAME, "screen").text
        assert result == "15"

    finally:
        driver.quit()
