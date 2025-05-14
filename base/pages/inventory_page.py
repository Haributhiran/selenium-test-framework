from selenium.webdriver.common.by import By
from base.pages.base_page import BasePage
from base.pages.login_page import LoginPage
from settings import Settings
import time

settings = Settings()

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "product_label")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    REMOVE_FROM_CART_BUTTON = (By.XPATH, "//button[text()='REMOVE']")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_ICON = (By.ID, "shopping_cart_container")

    def login_and_go_to_inventory(self):
        login_page = LoginPage(self.driver)
        login_page.go_to(settings.base_url)
        login_page.login(settings.username, settings.password)
        time.sleep(2)

    def get_title_text(self):
        return self.get_text(self.TITLE)

    def add_first_item_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def get_cart_count(self):
        if self.is_visible(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"

    def select_sort_option(self, visible_text):
        from selenium.webdriver.support.ui import Select
        dropdown = Select(self.find(self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(visible_text)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_all_product_names(self):
        elements = self.find_all(self.PRODUCT_NAMES)
        return [el.text for el in elements]

    def remove_first_item_from_cart(self):
        self.click(self.REMOVE_FROM_CART_BUTTON)


    def get_all_product_prices(self):
        elements = self.find_all((By.CLASS_NAME, "inventory_item_price"))
        return [float(el.text.replace("$", "")) for el in elements]
