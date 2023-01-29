import tweepy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from random import randint
from random import shuffle

os.chdir('/root/twitter')

consumer_key = 'gQztbTvdso9FYWX6glBdK84uX'
consumer_secret = 'zjQmfWbjl1TavwfWM8swXaqoEQT3zRorWpetYMkXLZVkC3fbBg'

key = '1432478133660397570-7csEyOrF2Op8QPl2PKXRW07PQ5JsDm'
secret = 'MItivm2VJuFDmFUEH4E7HgA7jV1L4jt6uq7ZMNYB4zg4r'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def newChromeBrowser(headless=True, downloadPath="/root/twitter/videos"):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('headless')
        if downloadPath is not None:
            prefs = {}
            prefs["profile.default_content_settings.popups"]=0
            prefs["download.default_directory"]=downloadPath
            options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return browser

def downloadVideo(vidlink):
    link = 'https://www.downloadtwittervideo.com/pt/'

    driver = newChromeBrowser()
    driver.get(link)

    search_box = driver.find_element(By.ID, "url")

    search_box.send_keys(vidlink)
    butt = driver.find_element(By.ID, "DownloadMP4HD")
    butt.click()
    time.sleep(5)

    
for message in api.get_direct_messages():
    vidlink = message.message_create['message_data']['entities']['urls'][0]['expanded_url']
    downloadVideo(vidlink=vidlink)
    messageid = message.id
    api.delete_direct_message(messageid)

    

accounts = ['HumansNoContext', 'CatWorkers', 'AAAAAGGHHHH', 'VideosFolder', 'DontShowYourCat', 'MediaTerrifying', 'mischiefanimals','256GBMemes','memeshorroroso', 'LocalBateman', '_ReplyDog','ShitpostGate','StrangestMedia', 'OutOfContextEvr']
shuffle(accounts)
inactives = ['perfectlyshots', 'lmfaoos', 'vid_img', 'hi1ar10us']
downloadCount = 0

for ac in accounts:
    if downloadCount > 6:
        break
    for tweet in api.user_timeline(screen_name=ac, exclude_replies=True, include_rts=False).reverse():
        if 'extended_entities' in tweet._json:
            if 'video_info' in tweet.extended_entities['media'][0]:
                downloadVideo(vidlink=tweet.entities['media'][0]['expanded_url'])
                downloadCount+=1
                break
            else:
                continue
        else:
            continue


for iac in inactives:
    for tweet in api.user_timeline(screen_name=ac, exclude_replies=True, include_rts=False).reverse():
        if 'extended_entities' in tweet._json:
            if 'video_info' in tweet.extended_entities['media'][0]:
                downloadVideo(vidlink=tweet.entities['media'][0]['expanded_url'])
            else:
                continue
        else:
            continue



for file in os.listdir('videos'):
    if file[0]+file[1]+file[2]+file[3]+file[4] == 'video':
        continue
    os.rename('videos/'+file, f'videos/video{randint(1000000, 9999999)}.mp4')
    