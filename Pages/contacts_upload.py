import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.signin import SignIn


class ContactImport:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _safe_click(self, element):
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def contact(self, url, email, password, file_path=None):
        if file_path is None:
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(project_root, "sample_contacts.csv")


        file_path = os.path.abspath(file_path)
        SignIn(self.driver).run(url, email, password)

        contact_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/aside/nav/a[2]')))
        self._safe_click(contact_button)

        upload_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/p[1]')))
        self._safe_click(upload_button)

        file_input = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/input')
        file_input.send_keys(file_path)
