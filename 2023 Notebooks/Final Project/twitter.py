# OAuth2.0 Version 
import tweepy

#Put your Bearer Token in the parenthesis below
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAG6tlQEAAAAAmDONPRv52vjJMXByLXMjA2RHkGc%3DHkP67Apz465sF4C5kOSotmAbChNGFpWnOfLkVlrQcDiDBivGdw')

"""
If you don't understand search queries, there is an excellent introduction to it here: 
https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/5-how-to-write-search-queries.md
"""

# Get tweets that contain the hashtag #petday
# -is:retweet means I don't want retweets
# lang:en is asking for the tweets to be in english
query = '#democrats -is:retweet lang:en'
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

"""
What context_annotations are: 
https://developer.twitter.com/en/docs/twitter-api/annotations/overview
"""
print('a')
for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)
print('aa')