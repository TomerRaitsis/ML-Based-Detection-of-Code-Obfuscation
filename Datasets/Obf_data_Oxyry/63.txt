from io import BytesIO #line:1
from tkinter import *#line:2
from tkinter import messagebox #line:3
import pygame #line:4
from random import *#line:5
from captcha .audio import AudioCaptcha #line:6
audio =AudioCaptcha ()#line:8
pygame .mixer .init ()#line:9
captcha_text =""#line:10
def create_audio_captcha ():#line:13
    global captcha_text #line:14
    captcha_text =str (randint (1000 ,9999 ))#line:15
    print (captcha_text )#line:16
    audio .write (captcha_text ,"audio"+".wav")#line:17
create_audio_captcha ()#line:20
root =Tk ()#line:22
root .title ("Audio Captcha")#line:23
def play_audio ():#line:26
    pygame .mixer .music .load ("audio"+".wav")#line:27
    pygame .mixer .music .play ()#line:28
def verify_audio ():#line:31
    O00O00O00O000O0OO =check .get ("1.0","end-1c")#line:32
    global captcha_text #line:33
    if O00O00O00O000O0OO ==captcha_text :#line:34
        messagebox .showinfo ("SUCCESS","Verified")#line:35
    else :#line:36
        messagebox .showinfo ("ALERT","Not Verified")#line:37
heading_label =Label (root ,text ="Enter the Audio Captcha",height =2 ,width =50 )#line:40
check =Text (root ,height =2 ,width =50 )#line:41
play_button =Button (root ,text ="Play Audio",command =play_audio )#line:42
submit =Button (root ,text ="Submit",command =verify_audio )#line:43
renew =Button (root ,text ="Renew",command =create_audio_captcha )#line:44
heading_label .pack ()#line:46
check .pack ()#line:47
play_button .pack (side =LEFT ,padx =35 ,pady =5 )#line:48
renew .pack (side =LEFT ,padx =40 ,pady =5 )#line:49
submit .pack (side =RIGHT ,padx =35 ,pady =5 )#line:50
root .mainloop ()#line:52
