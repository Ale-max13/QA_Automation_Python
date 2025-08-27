from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.cart_page import CartPage
from ..pages.checkout_page import CheckoutPage


def test_checkout_total(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack()
    inventory.add_tshirt()
    inventory.add_onesie()

    inventory.open_cart()
    cart.checkout()

    checkout.fill_step_one("Alena", "Kitaeva", "12345")

    assert checkout.get_total() == 58.29
