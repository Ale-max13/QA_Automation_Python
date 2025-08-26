import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")

    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def fill_step_one(self, first: str, last: str, postal: str):
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST)
            ).send_keys(first)
        self.driver.find_element(*self.LAST).send_keys(last)
        self.driver.find_element(*self.POSTAL).send_keys(postal)
        self.driver.find_element(*self.CONTINUE).click()

    def get_total(self) -> float:
        text = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        ).text
        m = re.search(r"[\d.]+", text)
        return float(m.group()) if m else 0.0

    def finish(self):
        self.driver.find_element(*self.FINISH).click()
