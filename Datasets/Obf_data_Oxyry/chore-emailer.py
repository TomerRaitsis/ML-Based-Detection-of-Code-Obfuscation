import random #line:1
import smtplib #line:2
def emailer (OO00OOOOOOOOOO0OO ,O0OO0O00000000O0O ):#line:5
    ""#line:12
    if not O0OO0O00000000O0O :#line:13
        print ("emails list should not be empty")#line:14
        return #line:15
    if not OO00OOOOOOOOOO0OO :#line:17
        print ("chores list should not be empty")#line:18
        return #line:19
    OO0O0OO0O0O0OO0OO ={}#line:21
    O0O00O000OOO0000O =0 #line:23
    while OO00OOOOOOOOOO0OO :#line:25
        O0O0000O00OO0OO0O =random .choice (OO00OOOOOOOOOO0OO )#line:27
        OO00OOOOOOOOOO0OO .remove (O0O0000O00OO0OO0O )#line:28
        OO00O0OO00OO00O00 =O0OO0O00000000O0O [O0O00O000OOO0000O ]#line:29
        OO0O0OO0O0O0OO0OO .setdefault (OO00O0OO00OO00O00 ,[])#line:30
        OO0O0OO0O0O0OO0OO [OO00O0OO00OO00O00 ].append (O0O0000O00OO0OO0O )#line:31
        O0O00O000OOO0000O =(O0O00O000OOO0000O +1 )%len (O0OO0O00000000O0O )#line:33
    OO00000O0OOOO0000 =smtplib .SMTP ("smtp.gmail.com",587 )#line:35
    OO00000O0OOOO0000 .ehlo ()#line:36
    OO00O0OO00OO00O00 =input ("Enter your email: ")#line:38
    OOOO0OO0OO0000O00 =input ("Enter your email password: ")#line:39
    OO00000O0OOOO0000 .starttls ()#line:41
    OO00000O0OOOO0000 .login (OO00O0OO00OO00O00 ,OOOO0OO0OO0000O00 )#line:42
    for O00O0O00OOOO00OOO ,O0000OO0O0O0O00OO in OO0O0OO0O0O0OO0OO .items ():#line:45
        OO000O0OO000O0OOO =", ".join (O0000OO0O0O0O00OO )#line:46
        print ("Sending email to %s..."%O00O0O00OOOO00OOO )#line:47
        OO00OOOO0000O0OOO =OO00000O0OOOO0000 .sendmail (OO00O0OO00OO00O00 ,O00O0O00OOOO00OOO ,"Subject: Your Chores.\nHi There!, {} are your chores".format (OO000O0OO000O0OOO ))#line:50
        if OO00OOOO0000O0OOO !={}:#line:51
            print ("There was a problem sending email to %s: %s"%(OO00O0OO00OO00O00 ,OO00OOOO0000O0OOO ))#line:54
    OO00000O0OOOO0000 .quit ()#line:56
if __name__ =="__main__":#line:59
    emailer (["dishes","bathroom","vacuum","walk dog"],["example@yahoo.com, example2@yahoo.com"],)#line:63
