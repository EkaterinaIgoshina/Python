from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_buttons = (By.CSS_SELECTOR, ".btn_primary.btn_inventory")
        self.cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_item_to_cart(self, item_index):
        buttons = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.add_to_cart_buttons)
        )
        buttons[item_index].click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()

