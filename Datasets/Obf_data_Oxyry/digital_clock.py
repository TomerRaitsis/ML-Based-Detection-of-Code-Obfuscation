import tkinter as tk #line:1
from time import strftime #line:2
def light_theme ():#line:5
    OO0O00OO0OOOO0000 =tk .Frame (root ,bg ="white")#line:6
    OO0O00OO0OOOO0000 .place (relx =0.1 ,rely =0.1 ,relwidth =0.8 ,relheight =0.8 )#line:7
    O0O000OOO000000O0 =tk .Label (OO0O00OO0OOOO0000 ,font =('calibri',40 ,'bold'),background ='White',foreground ='black')#line:9
    O0O000OOO000000O0 .pack (anchor ="s")#line:10
    def O0000OOO00OOOO0OO ():#line:12
        O0OOO0OOO00000OO0 =strftime ('%I:%M:%S %p')#line:13
        O0O000OOO000000O0 .config (text =O0OOO0OOO00000OO0 )#line:14
        O0O000OOO000000O0 .after (1000 ,O0000OOO00OOOO0OO )#line:15
    O0000OOO00OOOO0OO ()#line:16
def dark_theme ():#line:19
    OO00OOOO0OOOOOOO0 =tk .Frame (root ,bg ="#22478a")#line:20
    OO00OOOO0OOOOOOO0 .place (relx =0.1 ,rely =0.1 ,relwidth =0.8 ,relheight =0.8 )#line:21
    O00O0OOO00OO0OO0O =tk .Label (OO00OOOO0OOOOOOO0 ,font =('calibri',40 ,'bold'),background ='#22478a',foreground ='black')#line:23
    O00O0OOO00OO0OO0O .pack (anchor ="s")#line:24
    def O000O0O00O00O0O0O ():#line:26
        O0O00OO0OO0O00O00 =strftime ('%I:%M:%S %p')#line:27
        O00O0OOO00OO0OO0O .config (text =O0O00OO0OO0O00O00 )#line:28
        O00O0OOO00OO0OO0O .after (1000 ,O000O0O00O00O0O0O )#line:29
    O000O0O00O00O0O0O ()#line:30
root =tk .Tk ()#line:33
root .title ("Digital-Clock")#line:34
canvas =tk .Canvas (root ,height =140 ,width =400 )#line:35
canvas .pack ()#line:36
frame =tk .Frame (root ,bg ='#22478a')#line:38
frame .place (relx =0.1 ,rely =0.1 ,relwidth =0.8 ,relheight =0.8 )#line:39
lbl =tk .Label (frame ,font =('calibri',40 ,'bold'),background ='#22478a',foreground ='black')#line:41
lbl .pack (anchor ="s")#line:42
def time ():#line:44
    OO00OOO0O000OO0OO =strftime ('%I:%M:%S %p')#line:45
    lbl .config (text =OO00OOO0O000OO0OO )#line:46
    lbl .after (1000 ,time )#line:47
time ()#line:48
menubar =tk .Menu (root )#line:50
theme_menu =tk .Menu (menubar ,tearoff =0 )#line:51
theme_menu .add_command (label ="Light",command =light_theme )#line:52
theme_menu .add_command (label ="Dark",command =dark_theme )#line:53
menubar .add_cascade (label ="Theme",menu =theme_menu )#line:54
root .config (menu =menubar )#line:55
root .mainloop ()#line:56
