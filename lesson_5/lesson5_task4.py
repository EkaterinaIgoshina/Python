from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

#Перейти на страницу http://the-internet.herokuapp.com/login
driver.get("http://the-internet.herokuapp.com/login")

#Ввод значения в поле username
username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)
username_field.send_keys("tomsmith")

time.sleep(2)

#Ввод значения в поле password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

time.sleep(2)

#Нажатие кнопки Login
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

#Ожидание появления сообщения и вывод текста с зелёной плашки
success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
)
print(success_message.text)

#Закрыть браузер
driver.quit()
