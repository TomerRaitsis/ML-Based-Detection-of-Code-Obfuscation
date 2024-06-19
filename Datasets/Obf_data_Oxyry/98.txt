import tkinter as tk #line:1
from tkinter import filedialog #line:2
from PIL import Image ,ImageTk #line:3
import shutil #line:4
def open_image ():#line:8
    O00OOO00O0OO0OO00 =filedialog .askopenfilename ()#line:9
    if O00OOO00O0OO0OO00 :#line:10
        OOO0O0O0O00O0OOOO =Image .open (O00OOO00O0OO0OO00 )#line:11
        O0OOOOOOO0O0OOOOO =ImageTk .PhotoImage (OOO0O0O0O00O0OOOO )#line:12
        label .config (image =O0OOOOOOO0O0OOOOO )#line:13
        label .image =O0OOOOOOO0O0OOOOO #line:14
        global current_image_path #line:15
        current_image_path =O00OOO00O0OO0OO00 #line:16
def save_image ():#line:20
    if current_image_path :#line:21
        OOO0O000OO0OO00O0 =filedialog .asksaveasfilename (defaultextension =".png")#line:22
        if OOO0O000OO0OO00O0 :#line:23
            shutil .copy (current_image_path ,OOO0O000OO0OO00O0 )#line:24
root =tk .Tk ()#line:28
root .title ("Image Viewer and Transfer")#line:29
label =tk .Label (root )#line:32
label .pack ()#line:33
open_button =tk .Button (root ,text ="Open Image",command =open_image )#line:36
save_button =tk .Button (root ,text ="Save Image",command =save_image )#line:37
open_button .pack ()#line:38
save_button .pack ()#line:39
current_image_path =None #line:41
root .mainloop ()#line:43
