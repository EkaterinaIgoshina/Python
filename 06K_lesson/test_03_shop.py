from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_sauce_demo_checkout(browser):
    browser.get('https://www.saucedemo.com')

    browser.find_element(By.ID, 'user-name').send_keys('standard_user')
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()

    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    browser.find_element(By.ID, 'checkout').click()

    browser.find_element(By.ID, 'first-name').send_keys('Ekaterina')
    browser.find_element(By.ID, 'last-name').send_keys('Igoshina')
    browser.find_element(By.ID, 'postal-code').send_keys('601916')
    browser.find_element(By.ID, 'continue').click()

    total_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label'))
    )
    total = total_element.text

    assert total == 'Total: $58.29', f"Expected total to be $58.29, but got {total}"

if __name__ == "__main__":
    pytest.main()

