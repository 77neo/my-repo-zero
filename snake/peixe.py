from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


options = ChromeOptions()

options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_experimental_option('useAutomationExtension', False)

options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--user-data-dir=C:\\Users\\srcgo\\Desktop\\0\\selenium')
options.add_argument('--disable-dev-shm-usage') 
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://clip.cafe/iron-man-2008/tony-i-got-caught-doing-a-piece-vanity-fair/")
sleep(5)
driver.find_element(By.XPATH, '//*[@id="clip-info"]/div/a/button').click()
# b = driver.find_element(By.ID, "autocomplete")
# b.send_keys('iron man')
# sleep(3)
# b.submit()
# sleep(10)
sleep(4)