from cmath import log
import logging
import tweepy
import sys
import os

CONSUMER_KEY = os.environ.get('TWITTER_API_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_API_SECRET')
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

Logger = None
batch_size = 100

def main(args):
    global Logger
    logging.basicConfig(level=logging.WARN)
    Logger = logging.getLogger('get_tweets_by_id')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweets = api.user_timeline(args[0])


if __name__ == '__main__':
    main(sys.argv[1])