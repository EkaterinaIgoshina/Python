from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, ".btn_action.checkout_button")

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.checkout_button)
        ).click()

