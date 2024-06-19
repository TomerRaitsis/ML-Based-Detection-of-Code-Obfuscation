from tkinter import *#line:1
import datetime #line:2
import time #line:3
import os #line:4
root =Tk ()#line:5
def alarm (OO000O000OO0OO00O ):#line:6
    while True :#line:7
        time .sleep (1 )#line:8
        O00OOO0000O0OO00O =datetime .datetime .now ().time ()#line:9
        O00OOO0000O0OO00O =str (O00OOO0000O0OO00O )#line:10
        O00OOO0000O0OO00O =O00OOO0000O0OO00O [:5 ]#line:11
        if O00OOO0000O0OO00O ==OO000O000OO0OO00O :#line:12
            print ("Time to wake up")#line:13
            os .system ("start HeyYa.mp3")#line:14
            break #line:15
def actual_time ():#line:16
    OOOO0OO0OO00O0OOO =f"{hour.get()}:{minute.get()}"#line:17
    OOOO0OO0OO00O0OOO =str (OOOO0OO0OO00O0OOO )#line:18
    alarm (OOOO0OO0OO00O0OOO )#line:19
root .title ("Alarm clock")#line:20
root .geometry ("350x200")#line:21
hour =StringVar ()#line:22
minute =StringVar ()#line:23
Label (root ,text ="Hours   Min",font ="bold").place (x =10 )#line:24
hourTime =Entry (root ,textvariable =hour ,bg ="lightblue",fg ="black",font ="Arial",width =5 ).place (x =10 ,y =30 )#line:25
minuteTime =Entry (root ,textvariable =minute ,bg ="lightblue",fg ="black",font ="Arial",width =5 ).place (x =50 ,y =30 )#line:26
Label (root ,text ="Enter time in 24 hour format.",bg ="pink",fg ="black",font ="Arial").place (x =10 ,y =120 )#line:27
set =Button (root ,text ="Set alarm",fg ="black",width =10 ,command =actual_time ).place (x =10 ,y =70 )#line:28
root .mainloop ()