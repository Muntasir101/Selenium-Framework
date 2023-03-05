import time

import allure
from selenium import webdriver
from utils.common import get_config_value
from pages.LoginPage import LoginPage
from utils.logger import logger


@allure.feature("Login Feature")
def test_login():
    # Get the configuration settings
    url = get_config_value("DEFAULT", "url")
    print(url)
    browser = get_config_value("DEFAULT", "browser")
    headless = get_config_value("DEFAULT", "headless")

    # Initialize the web driver
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless == "True":
            options.add_argument("headless")
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Firefox()

    # Navigate to the login page
    driver.get(url)
    time.sleep(8)
    login_page = LoginPage(driver)

    # Enter the username and password
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")

    # Click the login button
    login_page.click_login_button()

    # Verify that the user is logged in
    assert "OrangeHRM" in driver.title

    # Log a debug message
    logger.debug('This is a debug message')

    # Log an info message
    logger.info('This is an info message')

    # Log a warning message
    logger.warning('This is a warning message')

    # Log an error message
    logger.error('This is an error message')

    # Log a critical message
    logger.critical('This is a critical message')

    # Quit the web driver
    driver.quit()
