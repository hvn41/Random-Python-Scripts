from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Take input from user
search_string = input("Input the URL or string you want to search for: ")

# To structure the string into search url
search_string = search_string.replace(' ', '+')

# --------------------DEPRECATED------------------------
# Assign browser variable with chromedriver of Chrome. 
# Other browser and its respective webdriver can be used.
# E.g. geckodriver for Mozilla Firefox
# --------------------DEPRECATED------------------------
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)

for i in range(1):
    matched_elements = browser.get("https://www.google.com/search?q=" + 
                                   search_string + "&start=" + str(i))