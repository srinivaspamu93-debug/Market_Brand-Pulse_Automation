import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignIn:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def run(self, url, username, password):
        if not url:
            url = os.getenv('LOGIN_URL')
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 15)
        email_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/form/div[1]/input')))
        email_input.send_keys(username)
        password_input = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div/div[2]/div/form/div[2]/input')
        password_input.send_keys(password)
        login_button = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div/div[2]/div/form/button')
        login_button.click()
