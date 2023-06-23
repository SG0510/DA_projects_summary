import os
import tweepy
import numpy as np
import pandas as pd
import json

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_SECRET']

auth = tweepy(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()

Tweet_screen_names = ['reading','jobready123','fridge','Indonesia']
alltweets = []

for sc_name in Tweet_screen_names:
    tweets = api.user_timeline(screen_name=sc_name, count=200)
    alltweets.extend(tweets)


# create a pandas dataframe from follows:
tweets_data = pd.DataFrame(data=[tweet.text for tweet in alltweets], columns=['Tweets'])
tweets_data['user_screen_name'] = np.array([tweet.user.screen_name for tweet in alltweets])
tweets_data['len'] = np.array([len(tweet.text) for tweet in alltweets])
tweets_data['ID'] = np.array([tweet.id for tweet in alltweets])
tweets_data['Date'] = np.array([tweet.created_at for tweet in alltweets])
tweets_data['source'] = np.array([tweet.source for tweet in alltweets])
tweets_data['hashtags'] = np.array([tweet.entities['hashtags'] for tweet in alltweets])
tweets_data['Likes'] = np.array([tweet.favorite_count for tweet in alltweets])
tweets_data['RTs'] = np.array([tweet.retweet_count for tweet in alltweets])

print(tweets_data.head(20))

tweets_data.to_csv("all_tweets.csv")