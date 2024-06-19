from selenium import webdriver #line:1
import requests as rq #line:2
import os #line:3
from bs4 import BeautifulSoup #line:4
import time #line:5
path =input ("Enter Path : ")#line:8
url =input ("Enter URL : ")#line:10
output ="output"#line:12
def get_url (OOO0O00O0O0OOOO00 ,O0O00OO00O0OO0OO0 ):#line:15
    O000000O0OO0OO00O =webdriver .Chrome (executable_path =r"{}".format (OOO0O00O0O0OOOO00 ))#line:16
    O000000O0OO0OO00O .get (O0O00OO00O0OO0OO0 )#line:17
    print ("loading.....")#line:18
    O00O00OOOOOOOOOOO =O000000O0OO0OO00O .execute_script ("return document.documentElement.outerHTML")#line:19
    return O00O00OOOOOOOOOOO #line:21
def get_img_links (O00OOOOO0O0OOOO0O ):#line:24
    OO0OO00OO0OO0O00O =BeautifulSoup (O00OOOOO0O0OOOO0O ,"lxml")#line:25
    OOOOO0O00O0O0OOO0 =OO0OO00OO0OO0O00O .find_all ("img",src =True )#line:26
    return OOOOO0O00O0O0OOO0 #line:27
def download_img (O0OO000OO00OOOOOO ,O0OO000O0O00O0000 ):#line:30
    try :#line:31
        O00O00O0OO0OOO0OO =[".jpeg",".jpg",".png",".gif"]#line:32
        OOO00O00O00000OOO =".jpg"#line:33
        for O00OO00000O00O00O in O00O00O0OO0OOO0OO :#line:34
            if O0OO000OO00OOOOOO .find (O00OO00000O00O00O )>0 :#line:35
                OOO00O00O00000OOO =O00OO00000O00O00O #line:36
                break #line:37
        OOO0000OO000OO00O =rq .get (O0OO000OO00OOOOOO ).content #line:39
        with open (output +"\\"+str (O0OO000O0O00O0000 +1 )+OOO00O00O00000OOO ,"wb+")as OO0OO0OO0O0OO0000 :#line:40
            OO0OO0OO0O0OO0000 .write (OOO0000OO000OO00O )#line:41
        OO0OO0OO0O0OO0000 .close ()#line:43
    except Exception :#line:44
        pass #line:45
result =get_url (path ,url )#line:48
time .sleep (60 )#line:49
img_links =get_img_links (result )#line:50
if not os .path .isdir (output ):#line:51
    os .mkdir (output )#line:52
for index ,img_link in enumerate (img_links ):#line:54
    img_link =img_link ["src"]#line:55
    print ("Downloading...")#line:56
    if img_link :#line:57
        download_img (img_link ,index )#line:58
print ("Download Complete!!")#line:59
