from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def add_backpack(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK)).click()

    def add_tshirt(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TSHIRT)).click()

    def add_onesie(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_ONESIE)).click()

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
        self.wait.until(EC.url_contains("/cart.html"))
