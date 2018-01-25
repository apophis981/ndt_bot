#!/usr/bin/python

import tweepy
#from auth import TwitterAuth
from markov_chain import markov
import imp

ndt_auth = imp.load_source('TwitterAuth', '../ndt_auth.py')

class TwitterAPI:
    def __init__(self):
        auth = tweepy.OAuthHandler(ndt_auth.TwitterAuth.consumer_key, ndt_auth.TwitterAuth.consumer_secret)
        auth.set_access_token(ndt_auth.TwitterAuth.access_token, ndt_auth.TwitterAuth.access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    tweet_string = markov.tweet
    print("Tweeting: " + tweet_string)
    twitter.tweet(markov.tweet)
