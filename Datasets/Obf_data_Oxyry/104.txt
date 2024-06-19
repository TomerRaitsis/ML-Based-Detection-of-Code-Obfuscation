#!/usr/bin/env python3
import cv2 #line:3
import numpy as np #line:4
import sys #line:6
symbols_list =["#","-","*",".","+","o"]#line:8
threshold_list =[0 ,50 ,100 ,150 ,200 ]#line:9
def print_out_ascii (O0O00O0OOO00O0OO0 ):#line:11
    ""#line:12
    for OO0OO0OOO0OO0O000 in O0O00O0OOO00O0OO0 :#line:14
        for OOOO0OO0O0OO0OO0O in OO0OO0OOO0OO0O000 :#line:15
            print (symbols_list [int (OOOO0OO0O0OO0OO0O )%len (symbols_list )],end ="")#line:17
        print ()#line:18
def img_to_ascii (O0O0O0000000O0OO0 ):#line:21
    ""#line:22
    O0000O0OOOOOOO0O0 ,O0O000OO00O000O00 =O0O0O0000000O0OO0 .shape #line:26
    O000OO000OOOOOO0O =int (O0O000OO00O000O00 /20 )#line:27
    OO00OO00OO0O00000 =int (O0000O0OOOOOOO0O0 /40 )#line:28
    OO00O00000000OOOO =cv2 .resize (O0O0O0000000O0OO0 ,(O000OO000OOOOOO0O ,OO00OO00OO0O00000 ),)#line:31
    OOOO0000000O00OO0 =np .zeros (OO00O00000000OOOO .shape )#line:33
    for OOOOO00O0OOO0O00O ,O00OO0OO00O00O000 in enumerate (threshold_list ):#line:35
        OOOO0000000O00OO0 [OO00O00000000OOOO >O00OO0OO00O00O000 ]=OOOOO00O0OOO0O00O #line:37
    return OOOO0000000O00OO0 #line:38
if __name__ =="__main__":#line:41
    if len (sys .argv )<2 :#line:43
        print ("Image Path not specified : Using sample_image.png\n")#line:44
        image_path ="sample_image.png"#line:45
    if len (sys .argv )==2 :#line:47
        print ("Using {} as Image Path\n".format (sys .argv [1 ]))#line:48
        image_path =sys .argv [1 ]#line:49
    image =cv2 .imread (image_path ,0 )#line:51
    ascii_art =img_to_ascii (image )#line:53
    print_out_ascii (ascii_art )#line:54
