from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    # Создаем объект страницы авторизации и выполняем действия
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Создаем объект главной страницы и добавляем товары в корзину
    main_page = MainPage(driver)
    main_page.add_item_to_cart(0)  # Sauce Labs Backpack
    main_page.add_item_to_cart(1)  # Sauce Labs Bolt T-Shirt
    main_page.add_item_to_cart(2)  # Sauce Labs Onesie

    # Переход в корзину
    main_page.go_to_cart()

    # Создаем объект страницы корзины и переходим к оформлению заказа
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Создаем объект страницы оформления заказа и заполняем форму
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_out_form("Ekaterina", "Igoshina", "601916")
    checkout_page.click_continue()

    # Проверка итоговой стоимости
    result = driver.find_element(By.CLASS_NAME,"summary_total_label").text
    result = result.replace("Total:","").replace("$","").strip()
    total_shop = "58.29"

    assert result == total_shop, f"Ожидалось '{total_shop}', но получили '{result}'"

    print(f"Полученное значение: '{result}'")

    # Закрыть браузер
    driver.quit()
