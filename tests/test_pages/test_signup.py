import pytest
import allure
import os
import time
from Pages.Signup import SignUp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Sign Up Feature")
@pytest.mark.order(2)
class TestSignUp:

    @allure.story("Successful Sign Up")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that a user can sign up with valid details.")
    def test_successful_sign_up(self, driver):
        url = os.getenv('SIGNUP_URL')
        username = "testuser" + str(int(time.time()))
        email = f"{username}@example.com"
        password = "TestPassword123"

        sign_up_page = SignUp(driver)

        with allure.step(f"Navigate to: {url}"):
            pass

        with allure.step("Perform sign up"):
            sign_up_page.run(url, username, email, password)

        with allure.step("Verify sign up success"):
            # Wait for potential redirect
            time.sleep(3)
            allure.attach(driver.get_screenshot_as_png(), name="sign_up_result",
                          attachment_type=allure.attachment_type.PNG)

            # Basic check: should not be on register page if successful
            # Note: actual assertion might need to be adjusted based on real app behavior
            assert "register" not in driver.current_url.lower(), f"Sign up failed, still on sign up page: {driver.current_url}"

    @allure.story("Failed Sign Up - Missing Email")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that a user cannot sign up without an email.")
    def test_failed_sign_up_missing_email(self, driver):
        url = os.getenv('SIGNUP_URL')
        username = "testuser_fail"
        email = ""
        password = "TestPassword123"

        sign_up_page = SignUp(driver)

        with allure.step("Perform sign up with missing email"):
            sign_up_page.run(url, username, email, password)

        with allure.step("Verify sign up failure"):
            time.sleep(2)
            allure.attach(driver.get_screenshot_as_png(), name="sign_up_failure",
                          attachment_type=allure.attachment_type.PNG)
            # Should still be on the register page
            assert "register" in driver.current_url.lower(), "Should still be on the register page after failed sign up"
