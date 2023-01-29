from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome()

driver.get('')