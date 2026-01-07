import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCalculator:
    @pytest.fixture(scope="class")
    def setup(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    def test_calculator(self, setup):
        self.driver = setup
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="7"]'))
       )

        input_field = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        input_field.clear()
        input_field.send_keys('45')

        button_seven = self.driver.find_element(By.XPATH, '//span[text()="7"]')
        button_seven.click()

        button_add = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.operator.btn.btn-outline-success'))
        )
        button_add.click()

        button_eight = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="8"]'))
       )
        button_eight.click()

        button_equals = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.btn.btn-outline-warning'))
        )
        button_equals.click()

        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.screen'))
        )

        # Ожидание, пока результат не изменится на '15'
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15')
        )

        result_element  = self.driver.find_element(By.CSS_SELECTOR, 'div.screen')
        result_text = result_element.text

        assert result_text == '15', f'Ожидалось 15, но получили {result_text}'
        print(f'Результат: {result_text}')












