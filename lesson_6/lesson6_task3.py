from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
element = WebDriverWait(driver, 40)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

element.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape"))
)
is_displayed = driver.find_element(By.CSS_SELECTOR,"#landscape").is_displayed()

print(is_displayed)

img = driver.find_element(By.CSS_SELECTOR, "#award")

print(img.get_attribute("src"))

driver.quit()

