# -*- coding: utf-8 -*-
import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def get_friends_descriptions(api, twitter_account, max_users):
    user_ids = []

    try:
        for page in tweepy.Cursor(api.followers_ids, id=twitter_account, count=5000).pages():
            user_ids.extend(page)

    except tweepy.RateLimitError:
        print ("RateLimitError...waiting 1000 seconds to continue")
        time.sleep(1000)
        for page in tweepy.Cursor(api.followers_ids, id=twitter_account, count=5000).pages():
            user_ids.extend(page)

    following = []

    for start in range(0, min(max_users, len(user_ids)), 100):
        end = start + 100

        try:
            following.extend(api.lookup_users(user_ids[start:end]))

        except tweepy.RateLimitError:
            print ("RateLimitError...waiting 1000 seconds to continue")
            time.sleep(1000)
            following.extend(api.lookup_users(user_ids[start:end]))

    for f in following:
        print(f)


if __name__ == "__main__":

    account_handle = 'low_sphinx'
    user_print_limit = 5

    print ("Reading data...")
    get_friends_descriptions(api, account_handle, max_users=user_print_limit)
