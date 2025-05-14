from base.pages.login_page import LoginPage
import time
from settings import Settings

settings = Settings()

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.go_to(settings.base_url)
    login_page.login(settings.username, settings.password)
    time.sleep(2)
    assert "inventory" in driver.current_url

def test_login_failed(driver):
    login_page = LoginPage(driver)
    login_page.go_to(settings.base_url)
    login_page.login(settings.username, "wrong_password")
    time.sleep(2)    
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"