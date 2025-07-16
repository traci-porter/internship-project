from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urljoin, urlparse

# Base URL to test
BASE_URL = "https://developer.kustomer.com/"

# Set up Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no browser UI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Visit the page
driver.get(BASE_URL)

# Get all <a> tags
anchor_tags = driver.find_elements(By.TAG_NAME, "a")
links = set()

# Collect href attributes
for tag in anchor_tags:
    href = tag.get_attribute("href")
    if href and href.startswith("http"):
        links.add(href)
    elif href and href.startswith("/"):
        links.add(urljoin(BASE_URL, href))  # Make relative URLs absolute

print(f"Found {len(links)} links. Checking for broken ones...\n")

# Check each link
for url in sorted(links):
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        status = response.status_code
        if status >= 400:
            print(f"[BROKEN] {url} — Status: {status}")
        else:
            print(f"[OK]     {url} — Status: {status}")
    except requests.RequestException as e:
        print(f"[ERROR]  {url} — Exception: {e}")

# Clean up
driver.quit()
