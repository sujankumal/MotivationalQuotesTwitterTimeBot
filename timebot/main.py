
from kivy.app import App
import tweepy
import threading
import time

from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class Home(Widget):
    display = StringProperty()
    
    def __init__(self,**kwargs):
        super(Home, self).__init__(**kwargs)
        
        self.check_safe = False
        
        self.api_key = "Js8FRc0gXfJB1OlReSeqCZQNY"
        self.api_key_secret = "M4WzoxYfKJOF37j7JbYqNt89CYMbf9eoeEMcnoHbZt51o9h8NV"
        self.access_token = "1048618625987465218-0XrSy0hAVTZb1XNxGjYywIdn1JTN6u"
        self.access_token_secret = "cXnnnYafERhceCq7xwlj9dqraYQKQmMawe3X0xFPnUFew"
        
        try: 
            self.auth = tweepy.OAuthHandler(self.api_key,
                self.api_key_secret)
            self.auth.set_access_token(self.access_token,
                self.access_token_secret)
            self.api = tweepy.API(self.auth)
        except Exception as e:
            print("Exception",str(e))
            self.print_display(str(e)+"\n")

    def print_display(self, text):
        t = str(self.display)
        if len(t)>1000:
            self.display = text
        else:
            self.display += text

    def split_string(str, limit, sep=" "):
        """
        Split String to length limit without breaking word
        """
        words = str.split(sep)
        if max(map(len, words)) > limit:
            raise ValueError("limit is too small")
        res, part, others = [], words[0], words[1:]
        for word in others:
            if len(sep)+len(word) > limit-len(part):
                res.append(part)
                part = word
            else:
                part += sep+word
        if part:
            res.append(part)
        return res

    def tweet(self):
        tweet_to_tweet = str(self.ids.tweet_input.text)
        tweet_length = len(tweet_to_tweet)
        if tweet_length == 0:
            self.print_display("tweet_length is 0")
            return

        print(tweet_to_tweet,"Fact Tweet Length: ", tweet_length)
        
        words = tweet_to_tweet.split(" ")
        if max(map(len, words)) > 280:
            raise ValueError("limit is too small")
        
        tweet_list, part, others = [], words[0], words[1:]
        for word in others:
            if len(" ")+len(word) > 280-len(part):
                tweet_list.append(part)
                part = word
            else:
                part += " "+word
        if part:
            tweet_list.append(part)
        
        tweet_obj = None
        try:
            for tweet in tweet_list:
                tweet_obj = self.api.update_status(status=tweet, in_reply_to_status_id= tweet_obj.id if tweet_obj else None)
        except Exception as e:
            print("Exception",str(e))
            self.print_display(str(e)+"\n")
        
        self.print_display(tweet_to_tweet + str("\n"))
        self.ids.tweet_input.text = ''

    def like_tweets(self):
        no_of_tweets = 100
        try:
            tweets = self.api.home_timeline(count=no_of_tweets)
        
            self.ids.progress_bar.value = 0
            tweet_processed = 0
            for tweet in tweets:
                self.print_display("("+tweet.user.screen_name+"): "+tweet.text+"\n")
                if tweet.in_reply_to_status_id is None:
                    # Not a reply, original tweet
                    if not tweet.favorited:
                        tweet.favorite()
                        self.print_display("Above tweet is liked.\n")
                        
                tweet_processed += 1
                self.ids.progress_bar.value = tweet_processed/no_of_tweets 
                time.sleep(0.15)

        except Exception as e:
            print("Exception",str(e))
            self.print_display(str(e)+"\n")

        
    def likeclick(self):
        t = threading.Thread(target=self.like_tweets).start()
        
class TimeBot(App):
    def build(self):
        
        return Home()


if __name__ == '__main__':
    TimeBot().run()