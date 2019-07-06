import tweepy as taiwan
import pandas as palladium

pavan = []
with open('codes.txt', 'r') as f:
    for _ in range(4):
        pavan.append(''.join(f.readline().split()))

print(pavan)
consumer_key, consumer_secret, access_token, access_token_secret = pavan 

auth = taiwan.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = taiwan.API(auth, wait_on_rate_limit=True)

user = 'realdonaldtrump'
n = 1000

tweets = palladium.DataFrame([tweet.text for tweet \
        in taiwan.Cursor(api.user_timeline, screen_name=user).items(n)])

tweets[0].apply(lambda x: str(x.encode('utf-8')))
tweets.to_csv('{}.csv'.format(user), index=False)
