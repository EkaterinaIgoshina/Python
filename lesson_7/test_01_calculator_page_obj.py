import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCalculator:
    @pytest.fixture(scope="class")
    def setup(self):
        # Инициализация драйвера
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(40)
        yield driver
        driver.quit()

    def test_calculator(self, setup):
        # Инициализация страницы калькулятора
        self.driver = setup
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

        calculator = CalculatorPage(self.driver)

        # Установка задержки на 45 секунд
        calculator.set_delay('45')

        # Выполнение вычисления 7 + 8
        calculator.click_button(calculator.button_seven)
        calculator.click_button(calculator.button_add)
        calculator.click_button(calculator.button_eight)
        calculator.click_button(calculator.button_equals)

        #Ожидание, пока результат не станет равным "15"
        WebDriverWait(self.driver,50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'div.screen'), "15")
        )

        #Получение результата
        result = self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text

        # Проверка результата
        assert result =='15', f'Ожидалось 15, но получили {result}'
        print(f'Результат: {result}')

