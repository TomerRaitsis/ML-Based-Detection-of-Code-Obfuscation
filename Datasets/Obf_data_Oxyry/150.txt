import webbrowser as wb #line:2
import tkinter as tk #line:3
from PIL import Image ,ImageTk #line:4
def button1_click ():#line:7
    print ("Button 1 clicked!")#line:8
    wb .open ("https://www.google.com/")#line:9
def button2_click ():#line:12
    print ("Button 2 clicked!")#line:13
    wb .open ("https://www.youtube.com/")#line:14
def button3_click ():#line:17
    print ("Button 3 clicked!")#line:18
    wb .open ("https://github.com/")#line:19
window =tk .Tk ()#line:23
button1_icon =ImageTk .PhotoImage (Image .open ("<ICON1_PATH>"))#line:26
button2_icon =ImageTk .PhotoImage (Image .open ("<ICON2_PATH>"))#line:27
button3_icon =ImageTk .PhotoImage (Image .open ("<ICON3_PATH>"))#line:28
button1 =tk .Button (window ,image =button1_icon ,command =button1_click )#line:31
button2 =tk .Button (window ,image =button2_icon ,command =button2_click )#line:32
button3 =tk .Button (window ,image =button3_icon ,command =button3_click )#line:33
button1 .pack ()#line:36
button2 .pack ()#line:37
button3 .pack ()#line:38
window .mainloop ()#line:41
