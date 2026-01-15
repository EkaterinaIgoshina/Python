from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы
    delay_input = (By.CSS_SELECTOR, '#delay')
    button_seven = (By.XPATH, '//span[@class="btn btn-outline-primary" and text()="7"]')
    button_add = (By.XPATH, '//span[@class="operator btn btn-outline-success" and text()="+"]')
    button_eight = (By.XPATH, '//span[@class="btn btn-outline-primary" and text()="8"]')
    button_equals = (By.XPATH, '//span[@class="btn btn-outline-warning" and text()="="]')

    def set_delay(self, delay):
        """Установить значение задержки."""
        delay_input = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#delay'))
        )
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_locator):
        """Нажать кнопку калькулятора."""
        button = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()




