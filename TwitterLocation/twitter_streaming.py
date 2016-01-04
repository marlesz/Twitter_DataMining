__author__ = 'ML'

import urllib3
urllib3.disable_warnings()
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "4299120508-arUXmZuiMOEs4vSJJMKLH9elAPAA0PdbVmXJLoO"
access_token_secret = "qIowLC1t7Dnr1bv0U6hMGfL7uaLbh76PFvbVStuK5RaKn"
consumer_key = "4WgOvRGQgxqAfGYyJklORwjnJ"
consumer_secret = "AlDanwtKk8iuvfCrAA2alYOMEL8fZ7qVHhZGtGXqEidhQ25x1C"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        with open('twitter_data.txt','a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['python', 'javascript', 'ruby'])
    stream.filter(locations=[-122.4440, 47.4792, -122.2421, 47.7592])

