from tkinter import W
import get_tweets
import get_content
import get_sentiment

def main():
    user_name = input('Enter Twitter user name: ')
    tweets = get_tweets.main(user_name)

    twt = ''
    for tweet in tweets:
        print(tweet.text)
        get_sentiment.sample_analyze_sentiment(tweet.text)
        twt += tweet.text

    get_content.analyze_content(twt)
    

if __name__ == '__main__':
    main()