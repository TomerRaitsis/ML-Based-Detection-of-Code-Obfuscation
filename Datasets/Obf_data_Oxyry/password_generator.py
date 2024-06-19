from tkinter import *#line:1
from random import choice #line:2
import string #line:3
class App :#line:5
    def __init__ (OO00OO0O0000OO0OO ):#line:6
        OO00OO0O0000OO0OO .window =Tk ()#line:7
        OO00OO0O0000OO0OO .window .title ('password_generator')#line:8
        OO00OO0O0000OO0OO .window .iconbitmap ('logo.ico')#line:9
        OO00OO0O0000OO0OO .window .iconphoto (False ,PhotoImage (file ='logo.png'))#line:10
        OO00OO0O0000OO0OO .window .geometry ('500x255')#line:11
        OO00OO0O0000OO0OO .window .config (bg ='gray')#line:12
        OO00OO0O0000OO0OO .label ()#line:15
        OO00OO0O0000OO0OO .entry ()#line:16
        OO00OO0O0000OO0OO .button ()#line:17
    def label (O00000OO00000O000 ):#line:19
        OOO0OOO000O0O000O =Label (O00000OO00000O000 .window ,text ='Welcome to password generator',font =('Courrier',20 ),bg ='gray',fg ='black')#line:20
        OOO0OOO000O0O000O .pack ()#line:21
    def entry (O0OO0O00OO0000OO0 ):#line:23
        O0OO0O00OO0000OO0 .password_entry =Entry (O0OO0O00OO0000OO0 .window ,font =('Courrier',25 ),bg ='white',fg ='black',width =30 ,relief ='solid')#line:24
        O0OO0O00OO0000OO0 .password_entry .pack (pady =50 )#line:25
    def button (OOOOO00000O0O0OO0 ):#line:27
        O00000OOOO0000OO0 =Button (OOOOO00000O0O0OO0 .window ,text ="Generate_password",font =('Courrier',12 ),bg ='white',fg ='black',width =25 ,command =OOOOO00000O0O0OO0 .generate_password )#line:28
        O00000OOOO0000OO0 .pack ()#line:29
    def generate_password (OO0OO000O0OOO0OOO ):#line:31
        O0O0000OO00OOO00O =string .ascii_letters +string .punctuation +string .digits #line:32
        O0O0OO000O0OO0O0O =""#line:33
        for OO00OO0000OOO0OOO in range (28 ):#line:34
            O0O0OO000O0OO0O0O +=choice (O0O0000OO00OOO00O )#line:35
        OO0OO000O0OOO0OOO .password_entry .delete (0 ,END )#line:36
        OO0OO000O0OOO0OOO .password_entry .insert (0 ,O0O0OO000O0OO0O0O )#line:37
app =App ()#line:40
app .window .mainloop ()#line:41
