import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    service = Service('msedgedriver.exe')
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+79588998877",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in fields.items():
        el = driver.find_element(By.NAME, name)
        el.clear()
        el.send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    zip_code_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )

    assert zip_code_div.text.strip() == "N/A", \
        "Zip code не равен 'N/A'!"
    assert "alert-danger" in zip_code_div.get_attribute("class"), \
        "Zip code не подсвечен красным (нет класса alert-danger)!"
