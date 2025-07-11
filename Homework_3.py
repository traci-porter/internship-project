# Practice with locators

driver.find_element(By.ID, 'nav-bb-logo') # Amazon logo
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small') # Create account
driver.find_element(By.CSS_SELECTOR, "label[for='ap_customer_name'].a-form-label") # Your name
driver.find_element(By.CSS_SELECTOR, "label[for='ap_email'].a-form-label") # Your email/phone number
driver.find_element(By.CSS_SELECTOR, "label[for='ap_password'].a-form-label") # Your password
driver.find_element(By.CSS_SELECTOR, "label[for='ap_password_check'].a-form-label") # Re-enter your password
driver.find_element(By.ID, 'continue') # Continue
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']") # Conditions of use link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']") # Privacy Notice link
driver.find_element(By.ID, 'ra-sign-in-link') # Sign in instead

