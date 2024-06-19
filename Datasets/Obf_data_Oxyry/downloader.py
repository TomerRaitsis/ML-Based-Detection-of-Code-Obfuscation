# !/usr/bin/env python
from selenium import webdriver #line:2
from webdriver_manager .chrome import ChromeDriverManager #line:3
import json #line:4
import requests #line:5
def get_driver ():#line:12
    O00000O00O00O0OO0 =webdriver .ChromeOptions ()#line:14
    OO0OO0O000000O0OO ={"recentDestinations":[{"id":"Save as PDF","origin":"local","account":""}],"selectedDestinationId":"Save as PDF","version":2 ,}#line:21
    O0OOOOOO0O000O0OO ={"printing.print_preview_sticky_settings.appState":json .dumps (OO0OO0O000000O0OO )}#line:24
    O00000O00O00O0OO0 .add_experimental_option ("prefs",O0OOOOOO0O000O0OO )#line:25
    O00000O00O00O0OO0 .add_argument ("--kiosk-printing")#line:26
    O0000O0O0000OO000 =webdriver .Chrome (executable_path =ChromeDriverManager ().install (),options =O00000O00O00O0OO0 )#line:31
    return O0000O0O0000OO000 #line:32
def download_article (O0OO00OOOO0OO0O00 ):#line:35
    O000000O0OOO0O0O0 =get_driver ()#line:36
    O000000O0OOO0O0O0 .get (O0OO00OOOO0OO0O00 )#line:37
    O000000O0OOO0O0O0 .execute_script ("window.print();")#line:40
    O000000O0OOO0O0O0 .close ()#line:41
if __name__ =="__main__":#line:44
    URL =input ("provide article URL: ")#line:45
    if requests .get (URL ).status_code ==200 :#line:47
        try :#line:48
            download_article (URL )#line:49
            print ("Your article is successfully downloaded")#line:50
        except Exception as e :#line:51
            print (e )#line:52
    else :#line:53
        print ("Enter a valid working URL")#line:54
