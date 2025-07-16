from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Selenium WebDriver in headless mode
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

try:
    # 1. Load the Kustomer developer site
    url = "https://developer.kustomer.com"
    driver.get(url)
    time.sleep(2)

    # 2. Check title
    assert "Kustomer" in driver.title
    print("✅ Title check passed.")

    # 3. Check for endpoint section like 'GET /customers'
    page_source = driver.page_source
    if "GET /customers" in page_source:
        print("✅ 'GET /customers' endpoint is visible.")
    else:
        print("❌ 'GET /customers' endpoint not found.")

    # 4. Check that code blocks exist
    code_blocks = driver.find_elements(By.CSS_SELECTOR, "pre code")
    if len(code_blocks) > 0:
        print(f"✅ Found {len(code_blocks)} code blocks.")
    else:
        print("❌ No code blocks found.")

    # 5. Test sidebar navigation links
    sidebar_links = driver.find_elements(By.CSS_SELECTOR, ".sidebar a")
    print(f"🧭 Found {len(sidebar_links)} sidebar links.")
    for i, link in enumerate(sidebar_links[:5]):  # Just test the first 5 for speed
        href = link.get_attribute("href")
        if href and href.startswith("https://developer.kustomer.com"):
            print(f"✅ Link #{i+1} is valid: {href}")
        else:
            print(f"⚠️ Link #{i+1} might be broken or missing: {href}")

    # 6. (Optional) Search test – adjust CSS selector if needed
    try:
        search_input = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
        search_input.send_keys("conversation")
        time.sleep(2)
        results = driver.find_elements(By.CSS_SELECTOR, ".search-result")
        if results:
            print(f"✅ Search returned {len(results)} result(s).")
        else:
            print("❌ Search returned no results.")
    except Exception as e:
        print(f"⚠️ Search input not found or not working: {e}")

except AssertionError as ae:
    print("❌ Assertion failed:", ae)

finally:
    driver.quit()
