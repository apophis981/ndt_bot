#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
from auth import TwitterAuth

#Twitter API credentials
TwitterAuth.consumer_key = "D3ogjbqfTtqKJZ8Qq7vsmjaV4"
TwitterAuth.consumer_secret = "L9EeRuA6pEWaCXi8P7FxFhRvVf8F6qzQ28zWroY0JXpNuMh9BC"
TwitterAuth.access_key = "332383602-47QHHJz1JIzb7JYtOvE4kbp5xdEbH7eanFUOTbnz"
TwitterAuth.access_secret = "BdWwEwmlXbXZj5S7kPULlnHe38Ozi4cHHKms3U6rhWkQo"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(TwitterAuth.consumer_key, TwitterAuth.consumer_secret)
	auth.set_access_token(TwitterAuth.access_key, TwitterAuth.access_secret)
	api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print "...%s tweets downloaded so far" % (len(alltweets))

	#transform the tweepy tweets into a 2D array that will populate the csv
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	#write the csv
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("neiltyson")