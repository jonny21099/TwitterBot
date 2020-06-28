import tweepy
import schedule
import time
import random

def main():
	CONSUMER_KEY = "0NBTSJRajwZ0JStVs7cerFFPG"
	CONSUMER_SECRET = "6PCzho21MrfBbpP1qt2OpzpmdZscbhJPpfcJMJgeTkzX7Jb1JW"
	ACCESS_TOKEN = "1277004639301365760-aUiAeW8KhSCIgHY1bX0lmTX4cSPzZO"
	ACCESS_TOKEN_SECRET = "npFEnkrxfHiYciLm0r2oDjHGAtkL4LNH4pQwm9XeMKuAe"
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	api = tweepy.API(auth)
	public_tweets = api.update_status("Testing %d" % random.randint(1,100))

def my_time():
	schedule.every(5).seconds.do(main)
	while True:
		schedule.run_pending()
		time.sleep(1)

my_time()

	# try:
	# 	redirect_url = auth.get_authorization_url()
	# except tweepy.TweepError:
	# 	print('Error! Failed to get request token.')

	# session.set('request_token', auth.request_token['oauth_token'])



