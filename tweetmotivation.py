"""
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

with open('MotivationalQuotesDatabase.csv', encoding="utf8") as csv_file:
    data = list(csv.reader(csv_file, delimiter=','))
    motivations = data[1:]
    line_count = 0
    
lines = len(motivations)

with open('Facts.txt',  encoding='utf8') as fact_file:
    facts = [line.rstrip() for line in fact_file.readlines()]
fact_lines = len(facts)

scheduler = sched.scheduler(time.time, time.sleep)


def split_string(str, limit, sep=" "):
    
    # Split String to length limit without breaking word
    
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
    scheduler.enter(600, 1, do_tweet, ('scheduler_',))
    
scheduler.enter(2, 1, do_tweet, ('scheduler',))
scheduler.run()
"""
    

import tweepy
import csv
import mysql.connector
from mysql.connector import errorcode
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


DB_NAME = 'motivation'

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'raise_on_warnings': True
}
scheduler = sched.scheduler(time.time, time.sleep)

def mysql_connect():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")       
        else:
            print(err)
        import sys
        sys.exit()
    
    cursor = cnx.cursor()
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        import sys
        sys.exit()
    return (cnx, cursor)
    
def execute_get_query(cnx,cursor, table, index):

    update_cursor = cnx.cursor(buffered=True)
    try:
        update_cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        import sys
        sys.exit()
    try:
        sql = "SELECT m_no FROM {table} WHERE used is NULL".format(table=table)
        update_cursor.execute(sql)
    except Exception as E:
        print(str(E))
    if update_cursor.rowcount == 0:
        sql_update_query = """Update {table} set used = null""".format(table=table)
        update_cursor.execute(sql_update_query)
        cnx.commit()
    update_cursor.close()
    ###
    try:
        sql = "SELECT * FROM {table} WHERE m_no = {index}".format(table=table, index=index)
        cursor.execute(sql)
    except Exception as E:
        print(str(E))
    return cursor.fetchone()

def execute_update_query_set_used(cursor, table, index):
    try:
        sql = "Update {table} set used = 1 WHERE m_no = {index}".format(table=table, index=index)
        cursor.execute(sql)
    except Exception as E:
        print(str(E))
    return cursor.fetchone()

def mysql_close(cnx, cursor):
    cursor.close()
    cnx.close()

def mysql_commit(cnx, cursor):
    cnx.commit()


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

motivation_lines = 46556
facts_lines = 3105
def do_tweet(sc): 
    print("\n Do Tweet. Sleep for 30 second.",time.asctime())
    time.sleep(30)
    if(random.getrandbits(1)):
        print("Fact")
        fact_index = random.randint(0,facts_lines)
        cnx, cursor = mysql_connect()
        tweet_to_tweet = execute_get_query(cnx,cursor,'facts',fact_index)
        if tweet_to_tweet[2]:
            print("continue facts")
            mysql_close(cnx, cursor)
            do_tweet("fact is used")
            return
        else:
            print("tweet and update facts")
            execute_update_query_set_used(cursor,'facts',fact_index)
            mysql_commit(cnx, cursor)
            mysql_close(cnx, cursor)

            fact_tweet = tweet_to_tweet[1]
            try:
                tweet_length = len(fact_tweet)
                print(fact_tweet,"Fact Tweet Length: ", tweet_length, "index:",fact_index)
                tweet_list = split_string(str=fact_tweet, limit=280)
                tweet_obj = None
                for tweet in tweet_list:
                    tweet_obj = api.update_status(status=tweet, in_reply_to_status_id= tweet_obj.id if tweet_obj else None)
            except Exception as e:
                print("Fact Tweet Exception: ", str(e))
                do_tweet("Fact Tweet Exception")
                return
        print("\n Schedule From Fact: ",time.asctime())
        scheduler.enter(90, 1, do_tweet, ('fact_Fact',))
        return
    ####################################################
    
    print("Motivation")
    motivation_index = random.randint(0,motivation_lines)
    
    cnx, cursor = mysql_connect()
    tweet_to_tweet = execute_get_query(cnx,cursor, 'motivation',motivation_index)
    if tweet_to_tweet[4]:
        print("continue motivation")
        mysql_close(cnx, cursor)
        do_tweet("motivation is used")
        return
    else:
        print("tweet and update motivation")
        execute_update_query_set_used(cursor, 'motivation',motivation_index)
        mysql_commit(cnx, cursor)
        mysql_close(cnx, cursor)
       
        tweet = tweet_to_tweet[1]+"\n- "+ tweet_to_tweet[2]
        try:
            tweet_length = len(tweet)
            print(tweet,"Motivation Tweet Length: ", tweet_length, "index:",motivation_index)
            tweet_list = split_string(str=tweet, limit=280)
            tweet_obj = None
            for tweet in tweet_list:
                tweet_obj = api.update_status(status=tweet, in_reply_to_status_id= tweet_obj.id if tweet_obj else None)
        except Exception as e:
            print("motivation Exception: ", str(e))
            do_tweet("Exception motivation")
            return
    print("\n Schedule from motivation: ",time.asctime())
    scheduler.enter(600, 1, do_tweet, ('scheduler_motivation',))
    
scheduler.enter(2, 1, do_tweet, ('scheduler',))
scheduler.run()