from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#Открыть браузер Chrom
driver = webdriver.Chrome()
#Перейти на страницу http://uitestingplayground.com/classattr
driver.get("http://uitestingplayground.com/classattr")
print("страница успешно загружена")

#Добавить задержку перед кликом
time.sleep(3)

#Кликнуть на синию кнопку Button
button = WebDriverWait(driver, timeout=10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
)
button.click()
print("Кнопка успешно нажата")


