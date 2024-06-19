from tkinter import *#line:1
import datetime #line:2
import time #line:3
import winsound #line:4
def Alarm (O0000OO000OOO000O ):#line:6
    while True :#line:7
        time .sleep (1 )#line:8
        O0000O00OO000O00O =datetime .datetime .now ()#line:9
        O0O0O0O0O0OO000O0 =O0000O00OO000O00O .strftime ("%H:%M:%S")#line:10
        O0O000O0O0OOO00OO =O0000O00OO000O00O .strftime ("%d/%m/%Y")#line:11
        OOO00OO0OOO00000O ="Current Time: "+str (O0O0O0O0O0OO000O0 )#line:12
        if O0O0O0O0O0OO000O0 ==O0000OO000OOO000O :#line:13
            winsound .PlaySound ("Music.wav",winsound .SND_ASYNC )#line:14
            break #line:15
def get_alarm_time ():#line:16
    O0O00O0O0O000000O =f"{hour.get()}:{min.get()}:{sec.get()}"#line:17
    Alarm (O0O00O0O0O000000O )#line:18
window =Tk ()#line:19
window .title ("Alarm Clock")#line:20
window .geometry ("400x160")#line:21
window .config (bg ="#922B21")#line:22
window .resizable (width =False ,height =False )#line:23
time_format =Label (window ,text ="Remember to set time in 24 hour format!",fg ="white",bg ="#922B21",font =("Arial",15 )).place (x =20 ,y =120 )#line:24
addTime =Label (window ,text ="Hour     Min     Sec",font =60 ,fg ="white",bg ="black").place (x =210 )#line:25
setYourAlarm =Label (window ,text ="Set Time for Alarm: ",fg ="white",bg ="#922B21",relief ="solid",font =("Helevetica",15 ,"bold")).place (x =10 ,y =40 )#line:26
hour =StringVar ()#line:27
min =StringVar ()#line:28
sec =StringVar ()#line:29
hourTime =Entry (window ,textvariable =hour ,bg ="#48C9B0",width =4 ,font =(20 )).place (x =210 ,y =40 )#line:30
minTime =Entry (window ,textvariable =min ,bg ="#48C9B0",width =4 ,font =(20 )).place (x =270 ,y =40 )#line:31
secTime =Entry (window ,textvariable =sec ,bg ="#48C9B0",width =4 ,font =(20 )).place (x =330 ,y =40 )#line:32
submit =Button (window ,text ="Set Your Alarm",fg ="Black",bg ="#D4AC0D",width =15 ,command =get_alarm_time ,font =(20 )).place (x =100 ,y =80 )#line:33
window .mainloop ()