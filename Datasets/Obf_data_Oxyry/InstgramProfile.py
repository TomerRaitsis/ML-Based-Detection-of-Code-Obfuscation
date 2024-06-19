import requests #line:1
from lxml import html #line:2
import re #line:3
import sys #line:4
def main (O0OOOOOOO0O0000O0 ):#line:7
    ""#line:10
    OO0OO0O0O0OO00OOO ="https://www.instagram.com/{}/?hl=en".format (O0OOOOOOO0O0000O0 )#line:11
    OO0O0OO000O0OO0O0 =requests .get (OO0OO0O0O0OO00OOO )#line:12
    O000O00OO0000000O =html .fromstring (OO0O0OO000O0OO0O0 .content )#line:13
    O0O000OO00000OOOO =O000O00OO0000000O .xpath ('//meta[starts-with(@name,"description")]/@content')#line:14
    if O0O000OO00000OOOO :#line:16
        O0O000OO00000OOOO =O000O00OO0000000O .xpath ('//meta[starts-with(@name,"description")]/@content')#line:17
        O0O000OO00000OOOO =O0O000OO00000OOOO [0 ].split (', ')#line:18
        O000O0O0OO0O00O0O =O0O000OO00000OOOO [0 ][:-9 ].strip ()#line:19
        O000000O0OO000000 =O0O000OO00000OOOO [1 ][:-9 ].strip ()#line:20
        OOOOO0OOO000OO00O =re .findall (r'\d+[,]*',O0O000OO00000OOOO [2 ])[0 ]#line:21
        OOO0OOOOO00O0O0O0 =re .findall (r'name":"\w*[\s]+\w*"',OO0O0OO000O0OO0O0 .text )[-1 ][7 :-1 ]#line:22
        OOOO0000000O0OOO0 =re .findall (r'"description":"([^"]+)"',OO0O0OO000O0OO0O0 .text )[0 ]#line:23
        O00O0O00000O0OOO0 ={'success':True ,'profile':{'name':OOO0OOOOO00O0O0O0 ,'profileurl':OO0OO0O0O0OO00OOO ,'username':O0OOOOOOO0O0000O0 ,'followers':O000O0O0OO0O00O0O ,'following':O000000O0OO000000 ,'posts':OOOOO0OOO000OO00O ,'aboutinfo':OOOO0000000O0OOO0 }}#line:35
    else :#line:36
        O00O0O00000O0OOO0 ={'success':False ,'profile':{}}#line:40
    return O00O0O00000O0OOO0 #line:41
if __name__ =="__main__":#line:45
    '''driver code'''#line:46
    if len (sys .argv )==2 :#line:48
        output =main (sys .argv [-1 ])#line:49
        print (output )#line:50
    else :#line:51
        print ('=========>Invalid paramaters Valid Command is<=========== \
        \npython InstagramProfile.py username')#line:53
