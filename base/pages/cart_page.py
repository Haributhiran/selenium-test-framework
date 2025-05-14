from selenium.webdriver.common.by import By
from base.pages.base_page import BasePage

class CartPage(BasePage):
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTONS = (By.XPATH, "//button[text()='REMOVE']")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//a[text()='Continue Shopping']")
    CHECKOUT_BUTTON = (By.XPATH, "//a[text()='CHECKOUT']")

    def get_all_cart_product_names(self):
        elements = self.find_all(self.PRODUCT_NAMES)
        return [el.text for el in elements]

    def remove_all_products(self):
        buttons = self.find_all(self.REMOVE_BUTTONS)
        for button in buttons:
            button.click()
    
    def assert_cart_is_empty(self):
        is_empty = self.element_not_present(self.PRODUCT_NAMES)
        assert is_empty, "Expected no items in cart, but some items are still present."

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
