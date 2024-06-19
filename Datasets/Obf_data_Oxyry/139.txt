import spacy #line:1
from spacy .lang .en .stop_words import STOP_WORDS #line:2
from string import punctuation #line:3
stop_words =list (STOP_WORDS )#line:5
nlp =spacy .load ("en_core_web_md")#line:6
def summarize (O00O0OOOOOO0000O0 ):#line:9
    O0O0O0O0O0O0O000O =""#line:10
    OO0OO0OOOOOOOOO00 =nlp (O00O0OOOOOO0000O0 )#line:11
    len (OO0OO0OOOOOOOOO00 )#line:12
    OO000OOO0O00000O0 =[O0O0000OOOOOO000O .text for O0O0000OOOOOO000O in OO0OO0OOOOOOOOO00 ]#line:13
    print (OO000OOO0O00000O0 )#line:14
    O0O0O0O0O0O0O000O =O0O0O0O0O0O0O000O +"\n"#line:16
    print (O0O0O0O0O0O0O000O )#line:17
    O00O00OO00O000O00 ={}#line:19
    for O000OO000O0OO000O in OO0OO0OOOOOOOOO00 :#line:20
        if O000OO000O0OO000O .text .lower ()not in stop_words :#line:21
            if O000OO000O0OO000O .text .lower ()not in O0O0O0O0O0O0O000O :#line:22
                if O000OO000O0OO000O .text not in O00O00OO00O000O00 .keys ():#line:23
                    O00O00OO00O000O00 [O000OO000O0OO000O .text ]=1 #line:24
                else :#line:25
                    O00O00OO00O000O00 [O000OO000O0OO000O .text ]+=1 #line:26
    print (O00O00OO00O000O00 )#line:27
    OOO0O00OO0OOO0OO0 =max (O00O00OO00O000O00 .values ())#line:29
    for O000OO000O0OO000O in O00O00OO00O000O00 .keys ():#line:30
        O00O00OO00O000O00 [O000OO000O0OO000O ]=O00O00OO00O000O00 [O000OO000O0OO000O ]/OOO0O00OO0OOO0OO0 #line:31
    O000O00O000OOO00O =[O0OO0O0O000000OOO for O0OO0O0O000000OOO in OO0OO0OOOOOOOOO00 .sents ]#line:32
    print (O000O00O000OOO00O )#line:33
    O00O0O0O000OOO000 ={}#line:35
    for OOO0O0OOO00O000O0 in O000O00O000OOO00O :#line:36
        for O000OO000O0OO000O in OOO0O0OOO00O000O0 :#line:37
            if O000OO000O0OO000O .text .lower ()in O00O00OO00O000O00 .keys ():#line:38
                if OOO0O0OOO00O000O0 not in O00O0O0O000OOO000 .keys ():#line:39
                    O00O0O0O000OOO000 [OOO0O0OOO00O000O0 ]=O00O00OO00O000O00 [O000OO000O0OO000O .text .lower ()]#line:40
                else :#line:41
                    O00O0O0O000OOO000 [OOO0O0OOO00O000O0 ]+=O00O00OO00O000O00 [O000OO000O0OO000O .text .lower ()]#line:42
    from heapq import nlargest #line:44
    O0OO00O0O0OO0OOO0 =int (len (O000O00O000OOO00O )*0.3 )#line:46
    print (O00O0O0O000OOO000 )#line:47
    O000OOO0OO00O00O0 =nlargest (O0OO00O0O0OO0OOO0 ,O00O0O0O000OOO000 ,key =O00O0O0O000OOO000 .get )#line:49
    O0O000OO000OO000O =[OO0OOOOOOOOO0OO00 .text for OO0OOOOOOOOO0OO00 in O000OOO0OO00O00O0 ]#line:50
    O000OOO0OO00O00O0 =" ".join (O0O000OO000OO000O )#line:51
    print (O000OOO0OO00O00O0 )#line:53
text =input ("Enter the text: ")#line:56
summarize (text )#line:57
