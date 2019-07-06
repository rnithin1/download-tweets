import tweepy as tw
import pandas as pd

consumer_key = "QvB7IOhonOZ4pHbtaqbb7rCy3"
consumer_secret = "kMcEpaGB5YWdAFPNHK4KqOMpEmbaSpnnOAtS0WxrF6neSSpedY"
access_token = "961154556058066944-gjzjmKHKzU86sVMGUV6kzrQFHZbREJ8"
access_token_secret = "uj3TAygkFULXVw3k5WCd1yQABl7afoXgrutHRwD3VSGfI"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

user = 'realdonaldtrump'
n = 1000

tweets = pd.DataFrame([tweet.text for tweet \
        in tw.Cursor(api.user_timeline, screen_name=user).items(n)])

tweets[0].apply(lambda x: str(x.encode('utf-8')))
tweets.to_csv('{}.csv'.format(user), index=False)
