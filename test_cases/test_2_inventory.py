from base.pages.login_page import LoginPage
from base.pages.inventory_page import InventoryPage
from settings import Settings
import time

settings = Settings()

def test_add_to_cart(driver):
    inventory = InventoryPage(driver)
    inventory.login_and_go_to_inventory()
    assert inventory.get_title_text() == "Products"
    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == "1"
    time.sleep(2)
    inventory.remove_first_item_from_cart()
    assert inventory.get_cart_count() == "0"
    time.sleep(2)


def test_sort_by_name_atoz(driver):
    inventory = InventoryPage(driver)
    inventory.login_and_go_to_inventory()
    inventory.select_sort_option("Name (A to Z)")
    time.sleep(2)
    names = inventory.get_all_product_names()
    assert names == sorted(names), f"Expected A→Z, got {names}"

def test_sort_by_name_ztoa(driver):
    inventory = InventoryPage(driver)
    inventory.login_and_go_to_inventory()
    inventory.select_sort_option("Name (Z to A)")
    time.sleep(2)
    names = inventory.get_all_product_names()
    assert names == sorted(names, reverse=True), f"Expected Z→A, got {names}"

def test_sort_by_price_low(driver):
    inventory = InventoryPage(driver)
    inventory.login_and_go_to_inventory()
    inventory.select_sort_option("Price (low to high)")
    time.sleep(2)
    prices = inventory.get_all_product_prices()
    assert prices == sorted(prices), f"Expected low→high, got {prices}"

def test_sort_by_price_high(driver):
    inventory = InventoryPage(driver)
    inventory.login_and_go_to_inventory()
    inventory.select_sort_option("Price (high to low)")
    time.sleep(2)
    prices = inventory.get_all_product_prices()
    assert prices == sorted(prices, reverse=True), f"Expected high→low, got {prices}"