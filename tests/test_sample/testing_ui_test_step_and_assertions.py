from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging
import time
import requests

# Assuming you have the HTML source in the 'html_source' variable
url = "https://www.linkedin.com/in/wardropmike/"
response = requests.get(url)
html_source = response.text
soup = BeautifulSoup(html_source, 'html.parser')

# Find the 'a' element with 'href="tel:8018931756"' in its text content
element = soup.find('a', string='href="tel:801num"')
assert element == 'href="tel:801num"'
# If the element is found, you can interact with it using Selenium
# if element:
#     # Your Selenium code here
# else:
#     print("Element not found")
