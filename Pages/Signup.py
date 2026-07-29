import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUp:
    def __init__(self, driver):
        self.driver = driver

    def run(self, url, user_name, email_id, password):
        if not url:
            url = os.getenv('SIGNUP_URL')
        if not isinstance(url, str):
            url = str(url)
        url = url.strip()
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 15)
        user_name_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/form/div[1]/input')))
        user_name_input.send_keys(user_name)
        email_input = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div/div[2]/div/form/div[2]/input')
        email_input.send_keys(email_id)
        password_input = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div/div[2]/div/form/div[3]/input')
        password_input.send_keys(password)
        sign_up_button = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div/div[2]/div/form/button')
        sign_up_button.click()
