import tweepy
import csv
import random
import sched, time

api_key = "Js8FRc0gXfJB1OlReSeqCZQNY"
api_key_secret = "M4WzoxYfKJOF37j7JbYqNt89CYMbf9eoeEMcnoHbZt51o9h8NV"

auth = tweepy.OAuthHandler(api_key, api_key_secret)

# client token

# try:
#     redirect_url = auth.get_authorization_url()
#     print(redirect_url)
# except tweepy.TweepError:
#     print('Error! Failed to get request token.')

# https://api.twitter.com/oauth/authorize?oauth_token=kZiYhgAAAAAA85S-AAABdIzlALU
# GET request for /?oauth_token=kZiYhgAAAAAA85S-AAABdIzlALU&oauth_verifier=9KIp4UHTH9ULlOK8qTPRRgRuzyw1oEZm

##############
# oauth_token = "gmQjkQAAAAAA85S-AAABdJBGpqY"
# oauth_verifier = "RdoSazBOsjDqcDPhYYD5655HdocKdxVr"

# verifier = oauth_verifier

# auth.request_token = { 'oauth_token' : oauth_token,
#                          'oauth_token_secret' : verifier }
# try:
#     auth.get_access_token(verifier)
# except Exception as e:
#     print('Error! Failed to get access token.', str(e))

# print(auth.access_token, auth.access_token_secret, auth.request_token)

##################
    
    
# Access Token
access_token = "1048618625987465218-0XrSy0hAVTZb1XNxGjYywIdn1JTN6u"
access_token_secret = "cXnnnYafERhceCq7xwlj9dqraYQKQmMawe3X0xFPnUFew"

auth.set_access_token(access_token, access_token_secret)

# ################
api = tweepy.API(auth)

with open('MotivationalQuotesDatabase.csv') as csv_file:
    data = list(csv.reader(csv_file, delimiter=','))
    motivations = data[1:]
    line_count = 0
    
lines = len(motivations)
scheduler = sched.scheduler(time.time, time.sleep)
def do_tweet(sc): 
    
    print("\n Do Tweet. Sleep for 30 second.",time.asctime())
    time.sleep(30)
    
    with open("lines_used.txt", "r") as file:
        lines_used = [line.rstrip() for line in file.readlines()]
    index = random.randint(0,lines)
    if index in lines_used: 
        do_tweet("is used")
        return
    else:    
        lines_used.append(str(index))
        print(sc ,len(lines_used), index,"\n", motivations[index][0]+"\n -"+ motivations[index][1])
        
        if len(lines_used) == lines:
            lines_used.clear()
        with open("lines_used.txt", "w+") as file:
            file.writelines("%s\n" % line for line in lines_used)

#       Create a tweet
        tweet = motivations[index][0]+"\n -"+ motivations[index][1]
        try:
            if(len(tweet)<=280):
                api.update_status(tweet)
            else:
                do_tweet('Tweet Length')
                return

        except Exception as e:
            if(e[0]['code'] != 186):
                print("Exception Tweet Length")
            else:
                print("Exception: ", str(e))
                do_tweet("Exception")
                return
    print("\n Schedule: ",time.asctime())
    scheduler.enter(90, 1, do_tweet, ('scheduler_',))
    
scheduler.enter(2, 1, do_tweet, ('scheduler',))
scheduler.run()