import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from settings import Settings
from base.pages.login_page import LoginPage

settings = Settings()

@pytest.fixture
def driver():
    service_obj = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service_obj, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# @pytest.fixture
# def setup_teardown():
#     service_obj = Service(executable_path=ChromeDriverManager().install())
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")
#     driver = webdriver.Chrome(service=service_obj, options=options)
#     driver.implicitly_wait(10)
#     login_page = LoginPage(driver)
#     login_page.login(settings.username, settings.password)
#     yield
#     login_page.logout()
#     driver.quit()
