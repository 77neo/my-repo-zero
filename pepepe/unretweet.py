import tweepy

consumer_key = 'DFA7TTu8unQ1RQVtDqC0c7L7w'
consumer_secret = 'ngcP1zVTBoEPE2iUvOAswRb3fT2XzwZBf8U8vJfO80LAEkiYjw'

key = '1357044455350616067-t0FeAMSXMpmVWzkPOb47H2cCZ3RCeD'
secret = 'ZtHMOfkkRkM3HMHSiVGJIPcN3zSvAmORPIaOnn8q190KP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


api.unretweet(api.user_timeline()[0].id)  