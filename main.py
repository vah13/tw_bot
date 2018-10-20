#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-user-timeline
#  - displays a user's current timeline.
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys
sys.path.append(".")
import config

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
import tweepy
from tweepy import OAuthHandler

access_token = '%%'
access_secret = '%%'
consumer_key = '%%'
consumer_secret = '%%'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
#-----------------------------------------------------------------------
# this is the user we're going to query.
#-----------------------------------------------------------------------
with open("twitter_name") as twn:
    users = twn.readlines()

with open("keyword") as kw:
    keywords = kw.readlines()
    
for user in users:
    try:
        for status in tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode='extended').items(30):
            # Process a single status
            twitt = status.full_text
            for keyword in keywords:
                if keyword.lower() in twitt.lower():
                    print("https://twitter.com/"+user, keyword)
    except Exception, ex:
        print ex.message, user
