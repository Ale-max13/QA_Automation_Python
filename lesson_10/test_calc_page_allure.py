import pytest
import allure
from selenium import webdriver
from CalcMainPageAllure import SlowCalculatorPage


@pytest.fixture
def driver():
    """Инициализация и завершение работы драйвера."""
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()


@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 1),
        ("9", "-", "3", "6", 1),
        ("4", "x", "5", "20", 2),
        ("8", "÷", "2", "4", 1),
    ],
)
@allure.title("Калькулятор: {num1} {operation} {num2} = {expected_result}")
@allure.description("Проверка корректности расчётов калькулятора при разных операциях.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_operations(driver, num1, operation, num2, expected_result, delay):
    """Тест проверяет корректность выполнения операций калькулятора."""
    page = SlowCalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        page.open()

    with allure.step(f"Устанавливаем задержку: {delay} сек"):
        page.set_delay(delay)

    with allure.step("Выполняем нажатия на кнопки"):
        page.click_button(num1)
        page.click_button(operation)
        page.click_button(num2)
        page.click_button("=")

    with allure.step("Проверяем результат"):
        page.wait_for_result(expected_result)
        actual = page.get_result()
        assert actual == expected_result, f"Ожидали {expected_result}, получили {actual}"
