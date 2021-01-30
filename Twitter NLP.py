# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:27:58 2021

@author: Sameer
"""

import tweepy 
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


api_key = 'Ao5bOlH9cyCcrvLOP5GnneVba'
api_secret = 'DkNyj2MqxI7UsK4n5L5k3irZMxZCYDroqQTNbA1MA8ZNm1HpGW'
access_token = '348416485-rlB3bVcPeMMvnRLqnaAXz23xTQUumaCzZCdMQcGH'
access_secret = 'p6DCAwCKmAGRfYhsLPMCSiBJxY0X5bWZCMZGhfWnInnVn'

twitter = tweepy.OAuthHandler(api_key, api_secret)
api = tweepy.API(twitter)



corpus_tweets = api.search("#oatmeal", count=10) 
for tweet in corpus_tweets:
    print(tweet.text)

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
users_locs
    
blob_object = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
analysis = blob_object.sentiment
print(analysis)


import pandas as pd
table_dict ={'Text': Text1,'Polarity': Polarity1,'Emotion':Emotion1}
df = pd.DataFrame(table_dict)
df
    
df.to_csv('emotionforDec2.csv',index=False)