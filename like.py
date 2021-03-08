import tweepy
import time

auth = tweepy.OAuthHandler('CONSUMER_KEY',
                           'CONSUMER_SECRET')
auth.set_access_token('ACCESS_KEY',
                      'ACCESS_SECRET')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Banque en ligne'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
