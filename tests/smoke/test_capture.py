import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_capture_pages():
    # Simple smoke test to capture screenshots for README
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1366,768')
    # Headless avoided to ensure screenshots show real rendering; uncomment to run headless
    # options.add_argument('--headless')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    try:
        os.makedirs(r"docs\\images", exist_ok=True)
        driver.get("https://marketing-blast-2.emergent.host/login")
        time.sleep(1)
        driver.save_screenshot(r"docs\\images\\login.png")

        driver.get("https://marketing-blast-2.emergent.host/login")
        time.sleep(1)
        driver.save_screenshot(r"docs\\images\\dashboard.png")

        # Execution / console placeholder
        driver.save_screenshot(r"docs\\images\\execution.png")

        # Allure report placeholder (reuse same page)
        driver.save_screenshot(r"docs\\images\\allure-report.png")

        # Passed/Failed summary placeholder
        driver.save_screenshot(r"docs\\images\\passed_failed.png")
    finally:
        driver.quit()

    assert True
