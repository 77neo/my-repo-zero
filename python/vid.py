
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# import tweepy

# consumer_key = 'gQztbTvdso9FYWX6glBdK84uX'
# consumer_secret = 'zjQmfWbjl1TavwfWM8swXaqoEQT3zRorWpetYMkXLZVkC3fbBg'

# key = '1432478133660397570-7csEyOrF2Op8QPl2PKXRW07PQ5JsDm'
# secret = 'MItivm2VJuFDmFUEH4E7HgA7jV1L4jt6uq7ZMNYB4zg4r'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(key, secret)
# api = tweepy.API(auth, wait_on_rate_limit=True)


def newChromeBrowser(headless=True, downloadPath="C:\\Users\\srcgo\\Downloads\\scripts\\python\\pasta"):
    """ Helper function that creates a new Selenium browser """
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('headless')
    if downloadPath is not None:
        prefs = {}
        prefs["profile.default_content_settings.popups"]=0
        prefs["download.default_directory"]=downloadPath
        options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=options)
    return browser

link = 'https://www.downloadtwittervideo.com/pt/'
vidlink = 'https://twitter.com/Alfunnyposts/status/1616134515876823064?s=20&t=1QI_a08VuotJ113M6qv0aw'


driver = newChromeBrowser()
driver.get(link)

search_box = driver.find_element(By.ID, "url")

search_box.send_keys(vidlink)
butt = driver.find_element(By.ID, "DownloadMP4HD")
butt.click()
time.sleep(5)
