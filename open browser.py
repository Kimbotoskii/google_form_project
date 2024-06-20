from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = "https://google.com/"
# path = "C:\Selenium\chromedriver-win64\chromedriver-win64"

driver = webdriver.Chrome() # Here
driver.get(url)
