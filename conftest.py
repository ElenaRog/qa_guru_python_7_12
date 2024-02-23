import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from utills import attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    from dotenv import load_dotenv
    load_dotenv()
    browser_version = "100.0"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "121.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        #command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        command_executor="http://192.168.0.17:4444/wd/hub",
        options=options
    )
    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
