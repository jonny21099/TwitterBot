import os
from dotenv import load_dotenv #download
import tweepy #download

def delete_all():
	load_dotenv("APIKEY.env")
	CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
	CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
	ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
	ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	for status in tweepy.Cursor(api.user_timeline).items():
		try:
			api.destroy_status(status.id)
			print("Deleted:%s" % status.id)
		except:
			print ("Failed to delete:%s" % status.id)

print("THIS WILL DELETE ALL YOUR TWEETS")
user_input = input("ARE YOU SURE YOU WANT TO DELETE ALL YOUR TWEETS?\nTYPE \"DELETE TWEETS\" TO DELETE ALL YOUR TWEETS\n")
if (user_input == "DELETE TWEETS"):
	delete_all()
