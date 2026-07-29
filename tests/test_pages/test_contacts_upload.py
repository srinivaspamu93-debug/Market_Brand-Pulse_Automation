import os
import time

import allure
from Pages.contacts_upload import ContactImport
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Contact Import")
class TestContactImport:

    @allure.story("Successful Contact Import")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that contacts can be imported successfully using a CSV file.")
    def test_successful_contact_import(self, driver):
        url = os.getenv("LOGIN_URL")
        email = os.getenv("LOGIN_EMAIL")
        password = os.getenv("LOGIN_PASSWORD")

        # Path to the CSV file in the project root
        project_root = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))
            )
        )
        csv_file = os.path.join(project_root, "sample contacts.csv")

        contact_upload_page = ContactImport(driver)

        with allure.step("Perform contact import process"):
            contact_upload_page.contact(
                url=url,
                email=email,
                password=password,
                file_path=csv_file
            )

        with allure.step("Verify import success"):
            WebDriverWait(driver, 10).until(EC.url_changes(url))
            allure.attach(
                driver.get_screenshot_as_png(),
                name="import_success_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

            assert "login" not in driver.current_url.lower(), \
                f"Should not be on login page, current URL: {driver.current_url}"