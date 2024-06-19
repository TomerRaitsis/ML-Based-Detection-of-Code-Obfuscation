import os #line:1
def findUnneeded (OOOO00O0OOOO0OO00 ,O0O000000OO00O0O0 ):#line:2
    ""#line:3
    O000OO0O0O0OOOOO0 =os .path .abspath (OOOO00O0OOOO0OO00 )#line:4
    for OOO000OO000OO00O0 in os .listdir (O000OO0O0O0OOOOO0 ):#line:5
        OO00O00OOO000O0OO =os .path .join (O000OO0O0O0OOOOO0 ,OOO000OO000OO00O0 )#line:6
        if os .path .isdir (OO00O00OOO000O0OO ):#line:7
            OOO0OOO0O00000O0O =getDirSize (OO00O00OOO000O0OO )#line:8
        else :#line:9
            OOO0OOO0O00000O0O =os .path .getsize (OO00O00OOO000O0OO )#line:10
        if OOO0OOO0O00000O0O >O0O000000OO00O0O0 :#line:11
            print (f"{OO00O00OOO000O0OO}: {OOO0OOO0O00000O0O}")#line:12
def getDirSize (O0O0O0OOO0OOO0OOO ):#line:13
    ""#line:14
    O0O00OO00O000O0O0 =0 #line:15
    for O0O000OOOOOO00O0O ,O0O0O00OOOO0O0OO0 ,O00O0O000O0000O0O in os .walk (O0O0O0OOO0OOO0OOO ):#line:16
        for OOOO0O00OOOOO000O in O00O0O000O0000O0O :#line:17
            O0OOO0OOOOOO00000 =os .path .join (O0O000OOOOOO00O0O ,OOOO0O00OOOOO000O )#line:18
            O0O00OO00O000O0O0 +=os .path .getsize (O0OOO0OOOOOO00000 )#line:19
    return O0O00OO00O000O0O0 #line:20
if __name__ =="__main__":#line:21
    findUnneeded ("..",1000 )#line:22
