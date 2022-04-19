from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class Home(Widget):
    display = StringProperty()

    def __init__(self,**kwargs):
        super(Home, self).__init__(**kwargs)
        
    def tweet(self):
        self.display += str(self.ids.tweet_input.text+"\n")
        self.ids.tweet_input.text = ''

    def likeclick(self):
        pass


class TimeBot(App):
    def build(self):
        
        return Home()


if __name__ == '__main__':
    TimeBot().run()