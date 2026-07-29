import pytest
import allure
import os
import time
from Pages.signin import SignIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Login Feature")
@pytest.mark.order(1)
class TestLogin:

    @allure.story("Successful Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that a user can login with valid credentials.")
    def test_successful_login(self, driver):
        url = os.getenv('LOGIN_URL')
        username = os.getenv('LOGIN_EMAIL')
        password = os.getenv('LOGIN_PASSWORD')

        login_page = SignIn(driver)

        with allure.step(f"Navigate to: {url}"):
            # SignIn.run handles navigation
            pass

        with allure.step("Perform login"):
            login_page.run(url, username, password)

        with allure.step("Verify login success"):
            # Wait for URL to change (away from login page)
            WebDriverWait(driver, 10).until(EC.url_changes(url))

            allure.attach(driver.get_screenshot_as_png(), name="login_result",
                          attachment_type=allure.attachment_type.PNG)
            print(driver.current_url)
            assert "login" not in driver.current_url.lower(), f"Login failed, still on login page: {driver.current_url}"

    @allure.story("Failed Login - Invalid Credentials")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that a user cannot login with invalid credentials.")
    def test_failed_login(self, driver):
        url = os.getenv('LOGIN_URL')
        username = "invalid_user@example.com"
        password = "wrong_password"

        login_page = SignIn(driver)

        with allure.step("Perform login with invalid credentials"):
            login_page.run(url, username, password)

        with allure.step("Verify login failure"):
            # We expect to stay on the login page
            time.sleep(2)  # Give it a moment to show error message
            allure.attach(driver.get_screenshot_as_png(), name="login_failure",
                          attachment_type=allure.attachment_type.PNG)
            assert "login" in driver.current_url.lower(), "Should still be on the login page after failed login"
