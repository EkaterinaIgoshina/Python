from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


edge_driver_path = r"C:\Users\igosh\PycharmProjects\Python\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))

def fill_form():

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.NAME, "first-name"))
    )

    print("Заполняем поле имени")
    driver.find_element(By.NAME, "first-name").send_keys("Иван")

    print("Заполняем поле фамилии")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")

    print("Заполняем адрес")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")

    print("Заполняем электронную почту")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")

    print("Заполняем номер телефона")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")

    print("Заполняем город")
    driver.find_element(By.NAME, "city").send_keys("Москва")

    print("Заполняем страну")
    driver.find_element(By.NAME, "country").send_keys("Россия")

    print("Заполняем должность")
    driver.find_element(By.NAME, "job-position").send_keys("QA")

    print("Заполняем компанию")
    driver.find_element(By.NAME, "company").send_keys("Skypro")


def test_form_submission():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    fill_form()


    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    print("Нажимаем кнопку 'Submit'")
    submit_button.click()

    # Ожидание появления элемента с ID "zip-code" после нажатия кнопки "Submit"
    zip_code_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
    )

    print("Форма успешно отправлена.")
    
    zip_code_style = zip_code_element.value_of_css_property("border-color")
    assert zip_code_style == "rgb(255,0,0)", f"Поле zip code не подсвечено красным, а подсвечено: {zip_code_style}"

    print("Проверка цвета поля zip code прошла успешно.")

    fields_to_check = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    for field in fields_to_check:
        element = driver.find_element(By.NAME,field)
        field_style = element.value_of_css_property("border-color")
        assert field_style == "rgp(0,128,0)", f"Поле {field} не подсвечено зелёным, а подсвечено: {field_style}"
        print(f"Проверка цвета поля {field} прошла успешно.")

if __name__ == "__main__":

        test_form_submission()

        driver.quit()










        driver.quit()





