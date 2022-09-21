from cmath import log
import logging
import tweepy
import sys
import os

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

Logger = None
batch_size = 20

def main():
    global Logger
    logging.basicConfig(level=logging.WARN)
    Logger = logging.getLogger('get_tweets_by_id')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    api = tweepy.API(auth)

    # try:
    #     api.verify_credentials()
    #     print('Successful Authentication')
    # except:
    #     print('Failed authentication')

    test_name = "elonmusk"
    tweets = api.user_timeline(screen_name = test_name, count=batch_size)
    for tweet in tweets:
        print(tweet.text, end = "\n\n")



if __name__ == '__main__':
    main()