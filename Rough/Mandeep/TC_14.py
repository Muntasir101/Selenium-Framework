
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser

config = configparser.ConfigParser()

config.read("locator_config.ini")

# 1. launching browser
driver = webdriver.Firefox()

# 2. Navigating to the URL
driver.get('https://automationexercise.com/')
driver.implicitly_wait(10)

# 3. Verifying that home page is visible successfully
assert "Automation Exercise" in driver.title

# 4. Adding products to cart
# element present or not
# element enable or not

# ID
# NAME
# CSS
# XPATH
try:
    #add_to_cart_locator = config.get('locators', 'add_to_cart_selector')
    add_to_cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-product-id="1"].add-to-cart')))
    add_to_cart.click()
except Exception:
    print(Exception)
    print("Bug!!! Add to cart Button is not displayed")

driver.close()

