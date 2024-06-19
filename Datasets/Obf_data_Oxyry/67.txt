import os #line:1
import shutil #line:2
import sys #line:3
import cv2 #line:4
class FrameCapture :#line:6
    ""#line:9
    def __init__ (OOOOOOO000O0O000O ,O0O0000O00OO0O0O0 ):#line:10
        ""#line:14
        OOOOOOO000O0O000O .directory ="captured_frames"#line:15
        OOOOOOO000O0O000O .file_path =O0O0000O00OO0O0O0 #line:16
        if os .path .exists (OOOOOOO000O0O000O .directory ):#line:17
            shutil .rmtree (OOOOOOO000O0O000O .directory )#line:18
        os .mkdir (OOOOOOO000O0O000O .directory )#line:19
    def capture_frames (OO000O00OOOO000OO ):#line:21
        ""#line:25
        OO0O00OOOO0O00000 =cv2 .VideoCapture (OO000O00OOOO000OO .file_path )#line:26
        O000OOOOO0O00O0O0 =0 #line:28
        O00O0O0O000000000 =1 #line:29
        while O00O0O0O000000000 :#line:31
            O00O0O0O000000000 ,O00O0OOOO000O0OO0 =OO0O00OOOO0O00000 .read ()#line:32
            O00O0O0000OOO00O0 =f'{OO000O00OOOO000OO.directory}/frame{O000OOOOO0O00O0O0}.jpg'#line:33
            cv2 .imwrite (O00O0O0000OOO00O0 ,O00O0OOOO000O0OO0 )#line:34
            O000OOOOO0O00O0O0 +=1 #line:36
if __name__ =='__main__':#line:38
    file_path =sys .argv [1 ]#line:39
    fc =FrameCapture (file_path )#line:40
    fc .capture_frames ()#line:41
