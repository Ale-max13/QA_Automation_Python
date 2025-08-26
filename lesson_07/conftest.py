import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument("--window-size=1280,900")
    options.add_argument("--incognito")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument(
        "--disable-features=PasswordManagerOnboarding,PasswordLeakDetection"
    )

    drv = webdriver.Chrome(options=options)
    drv.set_page_load_timeout(60)
    yield drv
    drv.quit()
