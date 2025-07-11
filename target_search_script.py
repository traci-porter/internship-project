from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://target.com')

# click on account button
driver.find_element(By.XPATH, "//a[@id='account-sign-in']").click()


# Click SignIn button
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

# Assert (Verification)
assert "Login: Target" in driver.title, f"Expected title to contain 'Login: Target', but got {driver.title}"

sleep(6)







