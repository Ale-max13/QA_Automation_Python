from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 25)
    wait.until(
        lambda d: all(
            img.get_attribute("src") and len(img.get_attribute("src")) > 0
            for img in d.find_elements(By.CSS_SELECTOR, "img")
        ) and len(d.find_elements(By.CSS_SELECTOR, "img")) == 4
    )

    images = driver.find_elements(By.CSS_SELECTOR, "img")
    third_img_src = images[2].get_attribute("src")

    print(third_img_src)

finally:
    driver.quit()
