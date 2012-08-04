from twitter import Twitter, TwitterError
from twitter.oauth import OAuth, write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance
import os

CONSUMER_KEY='PUiHBJAy0QhCnpq3KytncA'
CONSUMER_SECRET='9JVE1dOJOzx4HzPNByCaNSfkxWr5LbN1QOkOhJWZc'

oauth_filename = os.environ.get('HOME', '') + os.sep + '.twitter_oauth'
oauth_token, oauth_token_secret = read_token_file(oauth_filename)

twitter = Twitter(domain='search.twitter.com')
twitter.uriparts = ()

poster = Twitter(
	auth=OAuth(
		oauth_token, oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET),
		secure=True,
		api_version='1',
		domain='api.twitter.com')

last_id_replied = [tweet['in_reply_to_status_id'] for tweet in poster.statuses.user_timeline() if tweet['in_reply_to_status_id'] != None][0]
