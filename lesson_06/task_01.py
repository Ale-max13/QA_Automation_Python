from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://uitestingplayground.com/ajax")

    button = driver.find_element(By.CSS_SELECTOR, "button#ajaxButton")
    button.click()

    wait = WebDriverWait(driver, 15)
    element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "p.bg-success"),
            "Data loaded with AJAX get request."
        )
    )

    success_text = element.text
    print(success_text)

finally:
    driver.quit()
