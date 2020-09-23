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

with open('Facts.txt',  encoding='utf8') as fact_file:
    facts = [line.rstrip() for line in fact_file.readlines()]
fact_lines = len(facts)

scheduler = sched.scheduler(time.time, time.sleep)


def split_string(str, limit, sep=" "):
    """
    Split String to length limit without breaking word
    """
    words = str.split()
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


def do_tweet(sc): 
    
    print("\n Do Tweet. Sleep for 30 second.",time.asctime())
    time.sleep(30)
    if(random.getrandbits(1)):
        # Facts
        print("Fact")
        with open("fact_lines_used.txt", "r") as file:
            fact_lines_used = [line.rstrip() for line in file.readlines()]
        fact_index = random.randint(0,fact_lines)
        if fact_index in fact_lines_used: 
            do_tweet("fact is used")
            return
        else:    
            fact_lines_used.append(str(fact_index))
            print(sc ,len(fact_lines_used), fact_index,"\n", facts[fact_index])
            
            if len(fact_lines_used) == fact_lines:
                fact_lines_used.clear()
            with open("fact_lines_used.txt", "w+") as file:
                file.writelines("%s\n" % line for line in fact_lines_used)
            
            fact_tweet = facts[fact_index]
            try:
                tweet_length = len(fact_tweet)
                print("Tweet Length: ", tweet_length)
                # tweet_list = [fact_tweet[i:i+280] for i in range(0, tweet_length, 280)]
                tweet_list = split_string(str=fact_tweet, limit=280)
                tweet_obj = None
                for tweet in tweet_list:
                    tweet_obj = api.update_status(status=tweet, in_reply_to_status_id= tweet_obj.id if tweet_obj else None)
            
            except Exception as e:
                print("Fact Tweet Exception: ", str(e))
                do_tweet("Fact Tweet Exception")
                return
        print("\n Schedule From Fact: ",time.asctime())
        scheduler.enter(90, 1, do_tweet, ('fact_',))
        return
        
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
            tweet_length = len(tweet)
            print("Tweet Length: ", tweet_length)
            # tweet_list = [tweet[i:i+280] for i in range(0, tweet_length, 280)]
            tweet_list = split_string(str=tweet, limit=280)
            tweet_obj = None
            for tweet in tweet_list:
                tweet_obj = api.update_status(status=tweet, in_reply_to_status_id= tweet_obj.id if tweet_obj else None)
                
            
        except Exception as e:
            print("Exception: ", str(e))
            do_tweet("Exception")
            return
    print("\n Schedule: ",time.asctime())
    scheduler.enter(90, 1, do_tweet, ('scheduler_',))
    
scheduler.enter(2, 1, do_tweet, ('scheduler',))
scheduler.run()