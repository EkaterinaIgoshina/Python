from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

element = WebDriverWait(driver, 40)
element.until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'img'))
)
img_element = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#award"))
)
src_value = img_element.get_attribute("src")
print(src_value)
driver.quit()

