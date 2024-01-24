'''Python script for accessing twitter timeline and coding a bot'''
import tweepy
import time
# Authorization:
auth = tweepy.OAuthHandler('iDYIWzpeoRseTefBMLKSQL1T9',
                           'fT0AgEeoGx1sMtL7NtYCBwME3xCitLckBRT4hBU8mR0OKr7IL2')
auth.set_access_token('1750247018419634176-AvIVe11yNUCbMnCHUl9HnAPYuCs3IX',
                      'tDQbd5O9tu31TNxART45Fn1Zc15Qv6agqccYJzjZ9z9OX')
# creating an API object:
api = tweepy.API(auth)
user = api.me()
# Priniting basic info:
print(user.name)
print(user.screen_name)
print(user.followers)
# Priniting the tweets in timeline one by one:
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# Limit the amount of tweets to avoid crashing the twitter server:


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# Building a Bot to follow back:
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Pavan':
        print(follower.name)
        follower.follow()
    elif follower.followers_count > 100:
        follower.follow()
    else:
        follower.follow

# Building a bot to like the tweets and retweet it:
search_string = 'Python'
numberoftweets = 2
for tweet in tweepy.Cursor(api.search, search_string).items(numberoftweets):
    try:
        tweet.favorite()
        tweet.retweet()
        print('I liked that tweet!')
        print('I retweeted that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
