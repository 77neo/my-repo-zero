from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get('https://weilbyte.github.io/tiktok-tts/')

search_box = driver.find_element(By.ID, "text")

search_box.send_keys('The man, is the only creature that refuses to be what it is.')

select = Select(driver.find_element(By.ID,'voice'))

# select by value 
select.select_by_value('en_us_ghostface')

search_box.submit()


driver.execute_script('''
    // Javascript Code to create the anchor tag and download the file
    let aLink = document.createElement("a");
    let videoSrc = document.querySelector("audio").src;
    aLink.href = videoSrc;
    aLink.download = "";
    aLink.click();
    aLink.remove();
''')

time.sleep(10)