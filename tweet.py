import json
import tweepy
import koan
import openai_story

# Import configuration
config = json.load(open("config.json"))

# Authenticate to access the twitter API
client = tweepy.Client(
    consumer_key = config["credentials"]["api_key"],
    consumer_secret = config["credentials"]["api_key_secret"],
    access_token = config["credentials"]["access_token"],
    access_token_secret = config["credentials"]["access_token_secret"]
)

# Generate text
keywords = []
text = koan.get_koans(amount=1, keywords=keywords, sentences_per_book=20)[0]
prompt = f"An existential lovecraftian horror featuring a goat. {text}"
print(prompt)
tweet = openai_story.get_story(prompt)

# Tweet
response = client.create_tweet(text=tweet)
print(response)
