import tkinter #line:1
from time import strftime #line:2
top =tkinter .Tk ()#line:5
top .title ("Dynamic Clock")#line:6
top .resizable (0 ,0 )#line:7
def get_time_of_day (OOO00O0OO0OO0OO0O ):#line:11
    if 5 <=OOO00O0OO0OO0OO0O <12 :#line:12
        return "Morning"#line:13
    elif 12 <=OOO00O0OO0OO0OO0O <18 :#line:14
        return "Afternoon"#line:15
    else :#line:16
        return "Evening"#line:17
def update_time ():#line:21
    O0O00OOOO000O00O0 =strftime ("%H:%M:%S %p")#line:22
    OO00O00OO0O000O0O =int (strftime ("%H"))#line:23
    OOOO0O0000OO0O000 =get_time_of_day (OO00O00OO0O000O0O )#line:24
    clock_time .config (text =O0O00OOOO000O00O0 +f"\nGood {OOOO0O0000OO0O000}!")#line:27
    OOO0O00OOO00OOOOO =("lightblue"if OOOO0O0000OO0O000 =="Morning"else "lightyellow"if OOOO0O0000OO0O000 =="Afternoon"else "lightcoral")#line:34
    top .configure (background =OOO0O00OOO00OOOOO )#line:35
    clock_time .after (1000 ,update_time )#line:38
clock_time =tkinter .Label (top ,font =("courier new",40 ),background ="black",foreground ="white",)#line:47
clock_time .pack (anchor ="center")#line:50
update_time ()#line:53
top .mainloop ()#line:56
