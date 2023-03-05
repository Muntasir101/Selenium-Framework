import pytest
from selenium import webdriver
from utils.common import get_config_value


@pytest.fixture(scope="session")
def driver(request):
    """
    This fixture creates a WebDriver object and quits it when the test run is complete.
    """
    # Get the browser name and URL from the configuration file
    browser = get_config_value("test_settings", "browser")
    url = get_config_value("test_settings", "url")

    # Create a WebDriver object
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser '{browser}'")

    # Maximize the browser window
    driver.maximize_window()

    # Navigate to the URL
    driver.get(url)

    # Yield the driver object to the test functions
    yield driver

    # Quit the driver when the test run is complete
    driver.quit()
