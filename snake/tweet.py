import tweepy
import os
from datetime import datetime
import pytz
import random

os.chdir('/root/twitter')

consumer_key = 'gQztbTvdso9FYWX6glBdK84uX'
consumer_secret = 'zjQmfWbjl1TavwfWM8swXaqoEQT3zRorWpetYMkXLZVkC3fbBg'

key = '1432478133660397570-7csEyOrF2Op8QPl2PKXRW07PQ5JsDm'
secret = 'MItivm2VJuFDmFUEH4E7HgA7jV1L4jt6uq7ZMNYB4zg4r'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

videos = os.listdir('videos')
randNum = random.randint(0, len(videos)-1)
fileName = videos[randNum]

myLatestTweetTime = api.user_timeline()[0].created_at
currentTime = datetime.now(pytz.utc)

def tweet():
    for tweet in api.home_timeline(exclude_replies=True):
        tweetDate = tweet.created_at
        if 'RT ' in tweet.text:
            continue
        elif tweetDate.hour == currentTime.hour:
            if currentTime.minute - tweetDate.minute > 15:
                continue
        else:
            if currentTime.minute + (60 - tweetDate.minute) > 15:
                continue
        idT = tweet.id
        upload_result = api.media_upload(f'videos/{fileName}')
        api.update_status(status="",  in_reply_to_status_id=idT,media_ids=[upload_result.media_id_string],  auto_populate_reply_metadata=True)
        os.remove(f'videos/{fileName}')
        break

if currentTime.day == myLatestTweetTime.day:
    if (currentTime.hour - myLatestTweetTime.hour - 1)*60 + (60 - myLatestTweetTime.minute) + currentTime.minute >= 180:
        tweet()
else:
    if ((23 - myLatestTweetTime.hour) + currentTime.hour)*60 + (60 - myLatestTweetTime.minute) + currentTime.minute >= 180:
        tweet()