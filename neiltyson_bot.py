#!/usr/bin/python

import tweepy
from auth import TwitterAuth
from markov_chain import markov

class TwitterAPI:
    def __init__(self):
        auth = tweepy.OAuthHandler(TwitterAuth.consumer_key, TwitterAuth.consumer_secret)
        auth.set_access_token(TwitterAuth.access_token, TwitterAuth.access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    tweet_string = markov.tweet
    print "Tweeting: " + tweet_string
    twitter.tweet(markov.tweet)
