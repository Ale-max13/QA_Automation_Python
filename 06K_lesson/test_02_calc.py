import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_calc_addition(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    delay_input = driver.find_element(By.CSS_SELECTOR, "input#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    for symbol in ["7", "+", "8", "="]:
        driver.find_element(By.XPATH, f"//span[text()='{symbol}']").click()

    result = WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )
    assert result, "Результат не равен 15 через 45 секунд"
