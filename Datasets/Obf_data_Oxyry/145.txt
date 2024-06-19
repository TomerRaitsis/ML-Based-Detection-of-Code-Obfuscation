import tweepy #line:1
import time #line:2
print ("Testing The bot")#line:3
api_key ="enter your API key here"#line:4
api_secret ="enter your API secret key here"#line:5
access_token ="enter your access token here"#line:6
access_token_secret ="enter your access token secret here"#line:7
auth =tweepy .OAuthHandler (api_key ,api_secret )#line:8
auth .set_access_token (access_token ,access_token_secret )#line:9
api =tweepy .API (auth )#line:10
class MyStreamListener (tweepy .StreamListener ):#line:11
    def on_status (OO0000O000O00OO0O ,O0000OOO0O0000O00 ):#line:12
        if not O0000OOO0O0000O00 .retweeted and O0000OOO0O0000O00 .in_reply_to_status_id is None :#line:13
            print (O0000OOO0O0000O00 .text )#line:14
            try :#line:15
                api .retweet (O0000OOO0O0000O00 .id )#line:16
                print ("Retweeted")#line:17
            except tweepy .TweepError as O0000O00O0000O0OO :#line:18
                print (O0000O00O0000O0OO .reason )#line:19
    def on_error (OOO0O0000OO0OO000 ,OO000O000O0OOOOOO ):#line:20
        if OO000O000O0OOOOOO ==420 :#line:21
            print ("Error 420: Enhance Your Calm - Rate Limited")#line:22
            return False #line:23
myStreamListener =MyStreamListener ()#line:24
myStream =tweepy .Stream (auth =api .auth ,listener =myStreamListener )#line:25
keywords =["#Python","#python","#programming","#coding"]#line:26
myStream .filter (track =keywords ,languages =["en"])#line:27
