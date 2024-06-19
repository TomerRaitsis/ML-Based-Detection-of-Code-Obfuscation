import tkinter as tk #line:1
import pyperclip as pc #line:2
import webbrowser #line:3
Height =700 #line:5
Width =600 #line:6
root =tk .Tk ()#line:7
root .title ("Location Search")#line:8
canvas_color ="#FB6223"#line:9
frame_color ="#2DE3E9"#line:10
inner_frame_color ="#2EE3E9"#line:11
button_color ="#B8E82D"#line:12
entry_color ="#F2FECE"#line:13
font_ =("Handlee",16 )#line:14
def search_function (OO00OOOOO0OOO000O ):#line:17
    webbrowser .open ("https://google.com/maps/place/"+str (OO00OOOOO0OOO000O ))#line:18
canvas =tk .Canvas (root ,height =Height ,width =Width ,bg =canvas_color )#line:21
canvas .pack ()#line:22
frame =tk .Frame (root ,bg =frame_color ,bd =2 )#line:24
frame .place (relx =0.075 ,rely =0.1 ,relwidth =0.85 ,relheight =0.75 )#line:25
entry =tk .Entry (frame ,bg =entry_color ,font =font_ )#line:28
entry .place (relx =0.16 ,rely =0.1 ,relwidth =0.60 ,relheight =0.05 )#line:29
label =tk .Label (frame ,bg =canvas_color ,text ="Enter location to search",font =font_ )#line:31
label .place (relx =0.20 ,rely =0.2 )#line:32
button =tk .Button (frame ,font =font_ ,bg =button_color ,text ="Search",command =lambda :search_function (entry .get ()),)#line:41
button .place (relx =0.77 ,rely =0.1 ,relwidth =0.20 ,relheight =0.05 )#line:42
root .mainloop ()#line:44
