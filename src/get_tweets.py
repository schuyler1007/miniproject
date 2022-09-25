from cmath import log
import logging
import tweepy
import sys
import os

CONSUMER_KEY = os.environ['TWITTER_API_KEY']
CONSUMER_SECRET = os.environ['TWITTER_API_KEY_SECRET']
OAUTH_TOKEN = os.environ['TWITTER_CLIENT_ID']
OAUTH_TOKEN_SECRET = os.environ['TWITTER_CLIENT_SECRET']

Logger = None
batch_size = 20

def main(test_name):
    global Logger
    logging.basicConfig(level=logging.WARN)
    Logger = logging.getLogger('get_tweets_by_id')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    api = tweepy.API(auth)

    # test_name = "elonmusk"
    tweets = api.user_timeline(screen_name = test_name, count=batch_size)

    return tweets
    # for tweet in tweets:
    #     print(tweet.text, end = "\n\n")



# if __name__ == '__main__':
#     main()