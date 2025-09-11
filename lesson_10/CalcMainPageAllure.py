import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class SlowCalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_FIELD = (By.ID, "delay")
    RESULT_FIELD = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver) -> None:
        """Конструктор страницы калькулятора.

        :param driver: экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открываем страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.URL)

    def set_delay(self, seconds: int):
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_FIELD)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def _button_locator(self, label: str):
        return (By.XPATH, f"//span[normalize-space()='{label}']")

    def click_button(self, label: str):
        btn = self.wait.until(
            EC.element_to_be_clickable(self._button_locator(label))
        )
        btn.click()

    def get_result(self) -> str:
        result_elem = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_FIELD)
        )
        return result_elem.text.strip()

    def wait_for_result(self, expected: str):
        self.wait.until(lambda d: self.get_result() == expected)

