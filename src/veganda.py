# api token
import config

# imports
import tweepy

tweet = "Hello World"

# api
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SEC)
api = tweepy.API(auth)

api.create_friendship('martianmaikel')