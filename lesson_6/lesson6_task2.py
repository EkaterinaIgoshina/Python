from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/textinput')
input_field = driver.find_element(By.ID, 'newButtonName')
input_field.send_keys('SkyPro')

submit_button =  WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'btn-primary' ))
)
submit_button.click()

button_text = submit_button.text.strip()

print(button_text)

driver.quit()


