import tkinter as tk #line:1
from tkinter import filedialog #line:2
from PIL import Image #line:3
root =tk .Tk ()#line:4
root .title ('Converter')#line:5
canvas1 =tk .Canvas (root ,width =300 ,height =250 ,bg ='orange',relief ='raised')#line:6
canvas1 .pack ()#line:7
label1 =tk .Label (root ,text ='File Converter',bg ='lightsteelblue2')#line:8
label1 .config (font =('helvetica',20 ))#line:9
canvas1 .create_window (150 ,60 ,window =label1 )#line:10
im1 =None #line:11
def getJPG ():#line:14
    ""#line:15
    global im1 #line:16
    O000O00OO0O0O0OOO =filedialog .askopenfilename ()#line:17
    im1 =Image .open (O000O00OO0O0O0OOO )#line:18
font =('helvetica',12 ,'bold')#line:21
bg ='royalblue'#line:22
fg ='white'#line:23
browseButton_JPG =tk .Button (text ="      Import JPEG File     ",command =getJPG ,bg =bg ,fg =fg ,font =font )#line:24
canvas1 .create_window (150 ,130 ,window =browseButton_JPG )#line:25
def convertToPNG ():#line:28
    ""#line:29
    global im1 #line:30
    if im1 is None :#line:31
        tk .messagebox .showerror ("Error","No File selected")#line:32
    else :#line:33
        O00O0O0OOO0OO0O00 =filedialog .asksaveasfilename (defaultextension ='.png')#line:34
        im1 .save (O00O0O0OOO0OO0O00 )#line:35
saveAsButton_PNG =tk .Button (text ='Convert JPEG to PNG',command =convertToPNG ,bg =bg ,fg =fg ,font =font )#line:38
canvas1 .create_window (150 ,180 ,window =saveAsButton_PNG )#line:39
root .mainloop ()#line:40
