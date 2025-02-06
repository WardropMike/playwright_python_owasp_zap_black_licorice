from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging
import time

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Settings: INFO, DEBUG, WARNING, ERROR, CRITICAL Set the desired logging level

# Your logging script code starts here:
for i in range(5):
    logging.info(f"Processing item {i}")
    # Your other script logic...
# variables for steps:
expected_search_results_text = "Test Automation Using Python | Selenium Webdriver Tutorial"

# Create a Chrome WebDriver instance
try:
    driver = webdriver.Chrome()
except Exception as e:
    print("WebDriver Error:", e)
# Open Google's homepage
driver.get("https://testxcelerate.com")
time.sleep(5)
# Find the search input element and enter search criteria
input("Press Enter to continue...")
    # search_input1 = driver.find_element_by_id("textarea[title='search']")
    # search_input2 = driver.find_element(By.CSS, "textarea")
# try:
driver.find_element(By.CSS_SELECTOR, "button.rounded-md").click()
    # search_input2 = driver.find_element(By.CSS_SELECTOR, "button.rounded-md")
    # search_input3 = driver.find_element_by_link_text("I'm Interested!").click()
    # search_input2 = driver.find_element_by_css_selector("#input")
    # search_criteria = "Automated Testing with Selenium and python3 thats me!"
    # search_input3.send_keys(search_criteria)
# except Exception as e:
#     print("WebDriver Error:", e)

# Press Enter to perform the search
input("Press Enter to continue...")
# search_input.send_keys(Keys.RETURN)

# Assert that the search results page contains the search criteria
# css_selector = f"div > span:contains('{expected_search_results_text}')"
# search_results = driver.find_element_by_css_selector(css_selector)
css_selector = f"div > a:contains('href="tel:8018931756"')"
search_results = driver.find_element_by_css_selector(css_selector)
assert search_results == 'true'
print("Script completed.")
# Close the browser
# driver.quit()
