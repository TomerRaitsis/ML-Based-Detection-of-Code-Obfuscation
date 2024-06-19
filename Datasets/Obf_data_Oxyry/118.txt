import csv #line:1
from email .message import EmailMessage #line:2
import smtplib #line:3
def get_credentials (OOOO0OOOO0OO0O00O ):#line:6
    with open ("credentials.txt","r")as O000O0O0OO000OO00 :#line:7
        OOO000OOO000O0OOO =O000O0O0OO000OO00 .readline ()#line:8
        O0O00O000000O0000 =O000O0O0OO000OO00 .readline ()#line:9
    return (OOO000OOO000O0OOO ,O0O00O000000O0000 )#line:10
def login (OO00OOO0O000OOO00 ,O0OO0O0OOO0000O00 ,O0O0O0O00O000O000 ):#line:13
    O0O0O0O00O000O000 .ehlo ()#line:14
    O0O0O0O00O000O000 .starttls ()#line:16
    O0O0O0O00O000O000 .ehlo ()#line:17
    O0O0O0O00O000O000 .login (OO00OOO0O000OOO00 ,O0OO0O0OOO0000O00 )#line:19
    print ("login")#line:20
def send_mail ():#line:23
    O00OO0O00O000O0OO =smtplib .SMTP ("smtp.gmail.com",587 )#line:24
    O0O0O0000OO0OOOOO ,O000O0OO0OO0OOOOO =get_credentials ("./credentials.txt")#line:25
    login (O0O0O0000OO0OOOOO ,O000O0OO0OO0OOOOO ,O00OO0O00O000O0OO )#line:26
    OOOOO0O0O0OOO0OO0 ="Welcome to Python"#line:29
    O000OO0000000000O ="""Python is an interpreted, high-level,
    general-purpose programming language.\n
    Created by Guido van Rossum and first released in 1991,
    Python's design philosophy emphasizes code readability\n
    with its notable use of significant whitespace"""#line:34
    O0OOO0OO0OOO0O000 =EmailMessage ()#line:36
    O0OOO0OO0OOO0O000 .set_content (O000OO0000000000O )#line:37
    O0OOO0OO0OOO0O000 ['Subject']=OOOOO0O0O0OOO0OO0 #line:38
    with open ("emails.csv",newline ="")as OOO00OO00O000O0O0 :#line:40
        OOOOOO0O00OOO0O0O =csv .reader (OOO00OO00O000O0O0 ,delimiter =" ",quotechar ="|")#line:41
        for OO0000000O0O0O00O in OOOOOO0O00OOO0O0O :#line:42
            O00OO0O00O000O0OO .send_message (O0O0O0000OO0OOOOO ,OO0000000O0O0O00O [0 ],O0OOO0OO0OOO0O000 )#line:43
            print ("Send To "+OO0000000O0O0O00O [0 ])#line:44
    O00OO0O00O000O0OO .quit ()#line:47
    print ("sent")#line:48
if __name__ =="__main__":#line:51
    send_mail ()#line:52
