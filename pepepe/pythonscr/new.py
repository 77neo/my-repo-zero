from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep


options = ChromeOptions()
# options.add_argument("headless")
driver = webdriver.Chrome(options=options)

driver.get('https://www.tiktok.com/')
sleep(3)