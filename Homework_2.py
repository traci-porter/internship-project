from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Practice with locators

driver.find_element(By.ID, 'nav-logo-sprites') # Amazon logo
driver.find_element(By.ID, 'ap_email' ) # Email field
driver.find_element(By.ID, 'continue' ) # Continue button
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']") # Conditions of use link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']") # Privacy Notice link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']") # Need help link
driver.find_element(By.ID, 'auth-fpp-link-bottom') # Forgot your password link
driver.find_element(By.ID, 'ap-other-signin-issues-link') # Other issues with Sign-In link
driver.find_element(By.ID, 'createAccountSubmit') # Create your Amazon account button

