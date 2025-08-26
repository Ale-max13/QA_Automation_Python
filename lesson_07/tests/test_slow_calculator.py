from ..pages.slow_calculator_page import SlowCalculatorPage


def test_addition_7_plus_8(driver):
    page = SlowCalculatorPage(driver)
    page.open()
    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")
    page.wait_for_result("15")
    assert page.get_result() == "15"
