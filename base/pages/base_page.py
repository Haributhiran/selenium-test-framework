from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def go_to(self, url):
        self.driver.get(url)

    def find(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")

    def find_all(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Elements not found: {locator}")

    def click(self, locator):
        element = self.find(locator)
        element.click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def element_not_present(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until_not(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False