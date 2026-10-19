Practical 9 — Login Form Automation
Aim: Automate entering credentials and checking the login result.
This example uses a public practice login page. It is a demo account for testing, not a personal account.
Save as practical9.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
try:
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/secure")
    )
    if "/secure" in driver.current_url:
        print("Login Successful")
    else:
        print("Login Failed")
finally:
    driver.quit()
Run: python practical9.py. Expected terminal output: Login Successful. If the demo page changes or the login fails, inspect
the page and update the locators or credentials
