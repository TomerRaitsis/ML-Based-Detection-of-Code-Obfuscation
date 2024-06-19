import mysql .connector as c #line:1
con =c .connect (host ="",user ="",password ="")#line:3
cur =con .cursor ()#line:4
cur .execute ("use hillcipher")#line:5
def mod (O00000O0O00O00000 ):#line:9
    if O00000O0O00O00000 <0 :#line:10
        O000OOO00O00000OO =26 -(abs (O00000O0O00O00000 )%26 )#line:11
    else :#line:13
        O000OOO00O00000OO =O00000O0O00O00000 %26 #line:14
    return O000OOO00O00000OO #line:15
def hill_cipher (OO00OO0OO0000O00O ,OOOO0000OOO0OOO0O ):#line:21
    O0OO0OOO0OOOO0O00 =[]#line:22
    O0O00O000OO000OO0 =0 #line:23
    for OO0OO000OO000OO0O in range (3 ):#line:24
        O0O00O000OO000OO0 +=(OO00OO0OO0000O00O [OO0OO000OO000OO0O ]-1 )*OOOO0000OOO0OOO0O [OO0OO000OO000OO0O ]#line:25
    O0OO0OOO0OOOO0O00 .append (O0O00O000OO000OO0 )#line:26
    O0O00O000OO000OO0 =0 #line:28
    for OO0OO000OO000OO0O in range (3 ,6 ):#line:29
        O0O00O000OO000OO0 +=(OO00OO0OO0000O00O [OO0OO000OO000OO0O -3 ]-1 )*OOOO0000OOO0OOO0O [OO0OO000OO000OO0O ]#line:30
    O0OO0OOO0OOOO0O00 .append (O0O00O000OO000OO0 )#line:31
    O0O00O000OO000OO0 =0 #line:33
    for OO0OO000OO000OO0O in range (6 ,9 ):#line:34
        O0O00O000OO000OO0 +=(OO00OO0OO0000O00O [OO0OO000OO000OO0O -6 ]-1 )*OOOO0000OOO0OOO0O [OO0OO000OO000OO0O ]#line:35
    O0OO0OOO0OOOO0O00 .append (O0O00O000OO000OO0 )#line:36
    return O0OO0OOO0OOOO0O00 #line:37
def message (O0OOOOO00O0O0O0O0 ):#line:42
    OO0O0OO0O0OO000O0 =" "#line:43
    O0O00O0OOO00OOOOO =[]#line:44
    O0OOO0OOO00OO000O =[]#line:45
    for O0OOO00OO00OOOOO0 in range (3 ):#line:47
        O0O00O0OOO00OOOOO .append (O0OOOOO00O0O0O0O0 [O0OOO00OO00OOOOO0 ])#line:48
    for O0OOO00OO00OOOOO0 in range (3 ):#line:49
        cur .execute (f"select lid from loalpha where lchar = '{O0O00O0OOO00OOOOO[O0OOO00OO00OOOOO0]}'")#line:50
        O0O0OO0OO000OOOO0 =cur .fetchone ()#line:51
        for O0OOO00OO00OOOOO0 in O0O0OO0OO000OOOO0 :#line:52
            O0OOO0OOO00OO000O .append (O0OOO00OO00OOOOO0 )#line:53
    O0O0OO0OO000OOOO0 =[17 ,21 ,2 ,17 ,18 ,2 ,5 ,21 ,19 ]#line:55
    OOO0OO0OOO0O00O00 =hill_cipher (O0OOO0OOO00OO000O ,O0O0OO0OO000OOOO0 )#line:56
    for O0OOO00OO00OOOOO0 in OOO0OO0OOO0O00O00 :#line:58
        OOO00O000O0O0O00O =mod (O0OOO00OO00OOOOO0 )#line:59
        cur .execute (f"select lchar from loalpha where lid = {OOO00O000O0O0O00O+1}")#line:60
        OO0000O00OO0OO00O =cur .fetchone ()#line:61
        OO0O0OO0O0OO000O0 +=OO0000O00OO0OO00O [0 ]#line:63
    return OO0O0OO0O0OO000O0 #line:65
if __name__ =="__main__":#line:68
    Message =input ("enter your message")#line:69
    p =message (Message )#line:70
    print (p )#line:71
