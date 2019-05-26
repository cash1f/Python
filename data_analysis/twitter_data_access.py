import json

import dataset
from textblob import TextBlob

from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

consumer_key = 'zr4wI9IAme4AkhvwH5eofQ88A'
consumer_secret = 'daoUci9xD6Fk7T2VG3G1alqItyvw1W20KH4JPyy2X1zDTz3yF7'
access_token = '889363928555409408-hdzd7ze5GT4KBA4JXo13Qlg20FvWpww'
access_token_secret = 'xBGwruKHWrz5sXS62xdi0jIejqLNyIgmVhl6VZIhVo5zt'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#db = dataset.connect("sqlite:///tweets.db")
db = dataset.connect("sqlite:///gonawazgo.db")
class PrintListener(StreamListener):
    def on_status(self, status):
        if status.retweeted:
            return

        description = status.user.description
        loc = status.user.location
        text = status.text
        coords = status.coordinates
        geo = status.geo
        name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweets = status.retweet_count
        bg_color = status.user.profile_background_color
        blob = TextBlob(text)
        sent = blob.sentiment

        if geo is not None:
            geo = json.dumps(geo)

        if coords is not None:
            coords = json.dumps(coords)

        table = db['myTable']

        table.insert(dict(
                user_description=description,
                user_location=loc,
                coordinates=coords,
                text=text,
                geo=geo,
                user_name=name,
                user_created=user_created,
                user_followers=followers,
                id_str=id_str,
                created=created,
                retweet_count=retweets,
                user_bg_color=bg_color,
                polarity=sent.polarity,
                subjectivity=sent.subjectivity,
            ))
        print(text)

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True  # keep stream alive

    def on_timeout(self):
        print('Listener timed out!')
        return True  # keep stream alive


def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    stream.filter(languages=["en"], track=["gonenawazgone"])




def pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))

if __name__ == '__main__':
    print_to_terminal()
    #pull_down_tweets(auth.username)
