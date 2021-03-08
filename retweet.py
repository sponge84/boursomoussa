import tweepy
import time

auth = tweepy.OAuthHandler('SpvjMWuyDHxfhIT2puZWEmTuL',
                           'VHjaifIwLJN6lwxpuMFipnYBqXaRb6hMQzk96Y7nSeDRNfpR67')
auth.set_access_token('1366471105410707460-6IWSBatceoMD9pytSbRk5wFtlJAWTu',
                      'AXrF9W2UH0XITc3QpYALJcMZJM7TRl8C9OISxx8bg8PTe')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'BonPlan'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
