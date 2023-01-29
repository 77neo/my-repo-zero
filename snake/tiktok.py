from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_experimental_option('useAutomationExtension', False)

options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--enable-popup-blocking')

options.add_argument("user-data-dir=C:\\Users\\srcgo\\Desktop\\0\\selenium") 

driver = webdriver.Chrome(options=options)
driver.get("https://www.tiktok.com/upload")
sleep(5)
driver.maximize_window()
sleep(8)

iframe = driver.find_element(By.CSS_SELECTOR, 'iframe')
driver.switch_to.frame(iframe)

# Wait until page loads...
sleep(3)

# Select the input file and send the filename...
upload = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
video_path = 'C:/Users/my_video.mp4'
upload.send_keys('C:\\Users\\srcgo\\Desktop\\0\\video.mp4')
sleep(3)

capt = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div")
capt.click()
actions = ActionChains(driver)
actions.send_keys('dummydata vhhg')
actions.perform()
sleep(8)
e = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[8]/div[2]/button/div/div")
e.click()
sleep(30)
location = e.location
size = e.size
w, h = size['width'], size['height']

print(location)
print(size)
print(w, h)