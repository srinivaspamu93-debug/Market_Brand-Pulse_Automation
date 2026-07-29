from Pages.signin import SignIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from faker import Faker

class campaign_whatsapp:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver.maximize_window()

    def _safe_click(self, element):
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def campaign(self, url, email, password):
        login = SignIn(self.driver)
        login.run(url, email, password)

        # Click Campaign Button
        campaign_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[1]/a')))
        self._safe_click(campaign_button)

        # Campaign Name
        campaign_name_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/main/div/div[3]/div/input')))
        campaign_name_input.send_keys(Faker().text())

        # WhatsApp Campaign Type
        email_camp_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[3]/div/div[2]/button[2]')))
        self._safe_click(email_camp_button)

        next_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[4]/button[2]')))
        self._safe_click(next_button)

        # select all
        select_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,
                "//*[self::button or self::label or self::a]"
                "[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'select all')]")))
        self._safe_click(select_button)

        # click on next
        next_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[4]/button[2]')))
        self._safe_click(next_button)

        campaign_message_input = self.wait.until(
             EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/main/div/div[3]/div/div[1]/textarea'))
         )
        campaign_message_input.send_keys(Faker().text(110))

        next_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[4]/button[2]')))
        self._safe_click(next_button)

        send_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[3]/div/div[2]/button[1]'))
        )
        self._safe_click(send_button)




