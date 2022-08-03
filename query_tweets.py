import json
import tweepy

# Import configuration
config = json.load(open("config.json"))

# Variables for accessing twitter API
bearer_token = config["credentials"]["bearer_token"]
consumer_key = config["credentials"]["bearer_token"]
consumer_secret_key = config["credentials"]["bearer_token"]
access_token = config["credentials"]["bearer_token"]
access_token_secret = config["credentials"]["bearer_token"]

# Authenticate to access the twitter API
client = tweepy.Client(bearer_token)

# Search
query = "goat OR goats -is:retweet"
response = client.search_recent_tweets(query=query, max_results=25)
print(response)
