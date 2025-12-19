from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

#Перейти на страницу http://the-internet.herokuapp.com/inputs.
driver.get("http://the-internet.herokuapp.com/inputs")

input_field = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
)
#Ввод в поле текста "Sky"
input_field.send_keys("Sky")
time.sleep(3)

#Очистить поле
input_field.clear()

#Ввод в поле текста "Pro"
input_field.send_keys("Pro")

time.sleep(3)

#Закрыть браузер
driver.quit()
