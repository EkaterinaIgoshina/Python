from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.CSS_SELECTOR, ".btn_primary.cart_button")
        self.total_label = (By.CSS_SELECTOR, ".summary_subtotal_label")

    def fill_out_form(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        ).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.postal_code_input)
        ).send_keys(postal_code)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.continue_button)
        ).click()

    def get_total(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_label)
        ).text
