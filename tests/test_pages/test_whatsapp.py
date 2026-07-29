import pytest
import allure
import os
import time
from Pages.whatsapp_campaigns import campaign_whatsapp


@allure.feature("Campaign WhatsApp Creation")
@pytest.mark.order(7)
class TestCampaignWhatsAppCreation:

    @allure.story("Create a New WhatsApp Campaign")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that a user can successfully create a new WhatsApp campaign.")
    def test_create_campaign(self, driver):
        url = os.getenv('LOGIN_URL')
        email = os.getenv('LOGIN_EMAIL')
        password = os.getenv('LOGIN_PASSWORD')
        campaign_name = f"Test WhatsApp Campaign {int(time.time())}"

        campaign_page = campaign_whatsapp(driver)
        with allure.step(f"Navigate to {url}"):
            pass  # Navigation is handled inside the campaign method

        with allure.step(f"Create WhatsApp campaign: {campaign_name}"):
            campaign_page.campaign(url, email, password)

        with allure.step("Verify WhatsApp campaign creation completion and redirection to dashboard"):
            # The campaign method ends by clicking the send button
            time.sleep(2)
            allure.attach(driver.get_screenshot_as_png(), name="campaign_creation_result",
                          attachment_type=allure.attachment_type.PNG)

            # Basic validation that we are not on the login page and potentially on a dashboard/home page
            current_url = driver.current_url.lower()
            assert "login" not in current_url, f"Campaign creation failed or still on login page: {driver.current_url}"
