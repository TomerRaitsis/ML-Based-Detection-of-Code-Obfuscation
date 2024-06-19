import tkinter as tk #line:1
from math import sin ,cos ,pi #line:2
def update_clock ():#line:5
    O0OOOO0OOOOOOO00O =time_var .get ()#line:6
    O000O00OO000O0OOO =O0OOOO0OOOOOOO00O %60 #line:7
    O0O0OOO0OOOOO0O00 =(O0OOOO0OOOOOOO00O //60 )%60 #line:8
    OO0O0000O000O00O0 =(O0OOOO0OOOOOOO00O //3600 )%12 #line:9
    O0000000O00OOOOOO =90 -O000O00OO000O0OOO *6 #line:12
    OO0O0O0000O0O00O0 =90 -O0O0OOO0OOOOO0O00 *6 -O000O00OO000O0OOO *0.1 #line:13
    O000O0OO000OO00O0 =90 -(OO0O0000O000O00O0 *30 +O0O0OOO0OOOOO0O00 *0.5 )#line:14
    canvas .delete ("all")#line:16
    canvas .create_oval (50 ,50 ,250 ,250 )#line:18
    for O0000OO0OOOOOOOOO in range (1 ,13 ):#line:20
        OOOO0O0OOOOOO0O00 =90 -O0000OO0OOOOOOOOO *30 #line:21
        OOOO0000O0O00OOO0 =150 +85 *cos (OOOO0O0OOOOOO0O00 *(pi /180 ))#line:22
        O00OOO0O0O000OOOO =150 -85 *sin (OOOO0O0OOOOOO0O00 *(pi /180 ))#line:23
        canvas .create_text (OOOO0000O0O00OOO0 ,O00OOO0O0O000OOOO ,text =str (O0000OO0OOOOOOOOO ),font =("Arial",12 ,"bold"))#line:24
    draw_hand (150 ,150 ,O0000000O00OOOOOO ,80 ,1 )#line:26
    draw_hand (150 ,150 ,OO0O0O0000O0O00O0 ,70 ,2 )#line:27
    draw_hand (150 ,150 ,O000O0OO000OO00O0 ,50 ,4 )#line:28
    time_var .set (O0OOOO0OOOOOOO00O +1 )#line:30
    root .after (1000 ,update_clock )#line:32
def draw_hand (O000000O00OO0OOOO ,OO00OOOOO0OOO000O ,OOO00O000OO00O0O0 ,O00O000000O00O0O0 ,OOO0000OO0OO000OO ):#line:35
    O0OOO0OOOO000O00O =OOO00O000OO00O0O0 *(pi /180 )#line:36
    OOOO000OO00000000 =O000000O00OO0OOOO +O00O000000O00O0O0 *cos (O0OOO0OOOO000O00O )#line:37
    OO00O0O00OOOOO000 =OO00OOOOO0OOO000O -O00O000000O00O0O0 *sin (O0OOO0OOOO000O00O )#line:38
    canvas .create_line (O000000O00OO0OOOO ,OO00OOOOO0OOO000O ,OOOO000OO00000000 ,OO00O0O00OOOOO000 ,width =OOO0000OO0OO000OO )#line:39
root =tk .Tk ()#line:42
root .title ("Analog Clock")#line:43
canvas =tk .Canvas (root ,width =350 ,height =350 )#line:45
canvas .pack ()#line:46
time_var =tk .IntVar ()#line:48
time_var .set (10 *3600 )#line:49
update_clock ()#line:51
root .mainloop ()#line:52
