import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.CalculatorPage import CalculatorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCalculator:
    @pytest.fixture(scope="class")
    def setup(self):
        """ Инициализация драйвера. """

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(40)
        yield driver
        driver.quit()

    @allure.title("Тест калькулятора")
    @allure.description("Проверка функциональности калькулятора на сложение.")
    @allure.feature("Калькулятор")
    @allure.severity(allure.severity_level.NORMAL)

    def test_calculator(self, setup: webdriver.Chrome) -> None:
        """Проверка работы калькулятора."""

        self.driver = setup
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

        calculator = CalculatorPage(self.driver)

        with allure.step("Установка задержки на 45 секунд"):
            calculator.set_delay('45')

        with allure.step("Выполнение вычисления 7 + 8"):
            calculator.click_button(calculator.button_seven)
            calculator.click_button(calculator.button_add)
            calculator.click_button(calculator.button_eight)
            calculator.click_button(calculator.button_equals)

        with allure.step("Ожидание результата"):
            WebDriverWait(self.driver,50).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR,'div.screen'), "15")
            )

        with allure.step("Получение результата"):
            result = self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text

        with allure.step("Проверка результата"):
            assert result =='15', f'Ожидалось 15, но получили {result}'
            print(f'Результат: {result}')



