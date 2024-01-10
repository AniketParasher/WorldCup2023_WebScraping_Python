# Stepwise code working
The 1st step focuses on extracting match result data from the ICC Cricket World Cup 2023 tournament hosted on ESPN Cricinfo's website.

# Tools and Libraries Used
Python: Language used for scripting and automation.
Requests Library: Utilized to send HTTP requests and retrieve web pages.
BeautifulSoup (bs4): Employed for parsing HTML content and extracting required information.
HTML/CSS: Basic understanding of HTML tags and structure is beneficial for understanding the parsing process

# Process Overview
# Step 1: Retrieving Match Result Data

Requests Library
I employed the requests library to send an HTTP GET request to the specified URL. This allowed me to retrieve the HTML content of the web page programmatically.

BeautifulSoup (bs4)
Once the HTML content was retrieved, I utilized BeautifulSoup to create a soup object, enabling me to parse and navigate the HTML document.

# Step 2: Extraction Techniques
find_all()
The find_all() method in BeautifulSoup was used to locate all instances of specific HTML tags. It create that as a list.
find()
Similarly, the find() method was employed to target and extract the first occurrence of a particular HTML tag or class.

# Selenium
from selenium.webdriver.Chrome import ChromeOptions
ChromeOptions is imported from selenium.webdriver.Chrome to configure options for the Chrome web browser.  
options = ChromeOptions()
option.headless = True
driver = Chrome(options=options)
This code initiates an instance of the Chrome web browser using Selenium.

option.headless = True -> this code will help not to open chrome every time the loop run

driver.get('https://www.espncricinfo.com/cricketers/scott-edwards-1127317') - The get() function is used to instruct the web driver to navigate to the specified URL (https://www.espncricinfo.com/cricketers/scott-edwards-1127317 in this case).
