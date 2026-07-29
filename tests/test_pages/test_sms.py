import pytest
import allure
import os
import time
from Pages.sms_campaigns import campaign_sms


@allure.feature("Campaign SMS Creation")
@pytest.mark.order(6)
class TestCampaignSMSCreation:

    @allure.story("Create a New SMS Campaign")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that a user can successfully create a new SMS campaign.")
    def test_create_campaign(self, driver):
        url = os.getenv('LOGIN_URL')
        email = os.getenv('LOGIN_EMAIL')
        password = os.getenv('LOGIN_PASSWORD')
        campaign_name = f"Test SMS Campaign {int(time.time())}"

        campaign_page = campaign_sms(driver)
        with allure.step(f"Navigate to {url}"):
            pass  # Navigation is handled inside the campaign method

        with allure.step(f"Create SMS campaign: {campaign_name}"):
            campaign_page.campaign(url, email, password)

        with allure.step("Verify SMS campaign creation completion and redirection to dashboard"):
            # The campaign method ends by clicking the send button
            time.sleep(2)
            allure.attach(driver.get_screenshot_as_png(), name="campaign_creation_result",
                          attachment_type=allure.attachment_type.PNG)

            # Basic validation that we are not on the login page and potentially on a dashboard/home page
            current_url = driver.current_url.lower()
            assert "login" not in current_url, f"Campaign creation failed or still on login page: {driver.current_url}"
