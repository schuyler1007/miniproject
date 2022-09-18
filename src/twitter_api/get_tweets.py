from cmath import log
import logging
import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
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
