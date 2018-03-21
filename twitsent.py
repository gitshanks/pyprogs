import tweepy
from textblob import TextBlob

consumer_key = 'PCEvtBcdTR5EvHdIBuwoR2WsY'
consumer_secret = 'EkY0mbv6OcHg08iAZaamUJLdQsh1RGYNRshCoNFWb95AYmRn3Y'

access_token = '743417928926666753-xO58erx51A4hFDsD7yFpmhhAWfchaeF'
access_token_secret = 'Z4nrqew5pCb9U9DLFdC1tDgh3bw3RQxLGDfwQbCDqvyAS'

auth = tweepy.OAuthHandler( consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
 print(tweet.text)
 analysis = TextBlob(tweet.text)
 print(analysis.sentiment)