from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, ".btn_action")

    def enter_username(self, username: str) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def enter_password(self, password: str) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

    def click_login(self) -> None:
        self.driver.find_element(*self.login_button).click()




