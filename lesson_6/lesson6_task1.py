from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/ajax')

blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
blue_button.click()

green_banner = WebDriverWait(driver, 40).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success'))
)
banner_text = green_banner.text.strip()
print(banner_text)

driver.quit()








