import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@allure.title("Тест на оформление заказа")
@allure.description("Проверка процесса оформления заказа на сайте")
@allure.feature("Checkout")
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    with allure.step("Добавление товаров в корзину"):
        main_page = MainPage(driver)
        main_page.add_item_to_cart(0)
        main_page.add_item_to_cart(1)
        main_page.add_item_to_cart(2)

    with allure.step("Переход в корзину"):
        main_page.go_to_cart()

    with allure.step("Оформление заказа"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Заполнение формы оформления заказа"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_out_form("Ekaterina", "Igoshina", "601916")
        checkout_page.click_continue()

    with allure.step("Проверка итоговой стоимости"):
        result = driver.find_element(By.CLASS_NAME, "summary_total_label").text
        result = result.replace("Total:", "").replace("$", "").strip()
        total_shop = "58.29"

        assert result == total_shop, f"Ожидалось '{total_shop}', но получили '{result}'"

        print(f"Полученное значение: '{result}'")

    driver.quit()