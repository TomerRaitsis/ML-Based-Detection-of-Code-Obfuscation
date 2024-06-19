from tkinter import *#line:1
from tkinter import ttk #line:2
import calendar #line:3
def showCal ():#line:4
    O0O00OOO0OOOO0O0O =Tk ()#line:5
    O0O00OOO0OOOO0O0O .config (background ="white")#line:6
    O0O00OOO0OOOO0O0O .title ("Calendar")#line:7
    O0O00OOO0OOOO0O0O .geometry ("550x600")#line:8
    O00OO00O0O00O00OO =int (year_field .get ())#line:9
    OO0O00O0O00OO0000 =calendar .calendar (O00OO00O0O00O00OO )#line:10
    OOO0OOO0O0000O00O =Label (O0O00OOO0OOOO0O0O ,text =OO0O00O0O00OO0000 ,font ="Consolas 10 bold")#line:11
    OOO0OOO0O0000O00O .grid (row =5 ,column =1 ,padx =20 )#line:12
    O0O00OOO0OOOO0O0O .mainloop ()#line:13
if __name__ =="__main__":#line:14
    root =Tk ()#line:15
    root .config (background ="white")#line:16
    root .title ("HOME")#line:17
    root .geometry ("500x400")#line:18
    cal =Label (root ,text ="Welcome to the calendar Application",bg ="Green",font =("times",20 ,"bold"),)#line:19
    year =Label (root ,text ="Please enter a year",bg ="Green")#line:20
    year_field =Entry (root )#line:21
    Show =Button (root ,text ="Show Calendar",fg ="Black",bg ="Light Green",command =showCal )#line:22
    Exit =Button (root ,text ="Exit",fg ="Black",bg ="Light Green",command =exit )#line:23
    cal .grid (row =1 ,column =1 )#line:24
    year .grid (row =2 ,column =1 )#line:25
    year_field .grid (row =3 ,column =1 )#line:26
    Show .grid (row =4 ,column =1 )#line:27
    Exit .grid (row =6 ,column =1 )#line:28
    root .mainloop ()#line:29
