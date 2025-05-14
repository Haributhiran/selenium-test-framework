from base.pages.login_page import LoginPage
from base.pages.inventory_page import InventoryPage
from base.pages.cart_page import CartPage
from settings import Settings
import time

settings = Settings()

def login_and_add_items(driver):
    login_page = LoginPage(driver)
    login_page.go_to(settings.base_url)
    login_page.login(settings.username, settings.password)
    inventory = InventoryPage(driver)
    inventory.add_first_item_to_cart()
    time.sleep(3)
    inventory.go_to_cart()
    return CartPage(driver)


def test_products_exist_in_cart(driver):
    cart_page = login_and_add_items(driver)
    items = cart_page.get_all_cart_product_names()
    assert len(items) > 0, "No products found in cart."


def test_remove_products_from_cart(driver):
    cart_page = login_and_add_items(driver)
    cart_page.remove_all_products()
    cart_page.assert_cart_is_empty()


def test_continue_shopping_button(driver):
    cart_page = login_and_add_items(driver)
    cart_page.click_continue_shopping()
    assert "inventory" in driver.current_url, "Did not return to inventory page."


def test_cart_checkout(driver):
    cart_page = login_and_add_items(driver)
    cart_page.click_checkout()
    assert "checkout-step-one" in driver.current_url, "Did not navigate to checkout page."
