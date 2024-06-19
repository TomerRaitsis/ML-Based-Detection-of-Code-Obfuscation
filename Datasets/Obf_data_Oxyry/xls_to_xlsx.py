import os #line:1
from pathlib import Path #line:2
from win32com .client import Dispatch #line:3
def convert_xls_to_xlsx (O0OO0OO00OOOOOO00 :str ,file_format :int =51 ):#line:6
    ""#line:13
    O0O00O0O0OOO00O00 =Dispatch ("Excel.Application")#line:14
    O0O00O0O0OOO00O00 .Visible =False #line:15
    O00OOOOO00000OO0O =str (O0OO0OO00OOOOOO00 )+"x"#line:16
    OO0O0OO0OO0O0OO00 =O0O00O0O0OOO00O00 .Workbooks .Open (O0OO0OO00OOOOOO00 )#line:17
    OO0O0OO0OO0O0OO00 .SaveAs (O00OOOOO00000OO0O ,FileFormat =file_format )#line:18
    OO0O0OO0OO0O0OO00 .Close ()#line:19
    O0O00O0O0OOO00O00 .Quit ()#line:20
def remove_old_file (OOOO0OOOOO000O0O0 :str ):#line:23
    ""#line:28
    Path (OOOO0OOOOO000O0O0 ).unlink (missing_ok =False )#line:29
def main ():#line:32
    O0O00OOO0000O0000 =str (input ("Input the '.xls' file path:\n"))#line:33
    convert_xls_to_xlsx (file_path =O0O00OOO0000O0000 )#line:34
    OOO0O000O0OOOO00O =os .path .basename (O0O00OOO0000O0000 )#line:36
    print (f"Successfully converts {OOO0O000O0OOOO00O}")#line:37
    OOOOOO000O0O0OO00 =str (input (f"Do you want to delete the old {OOO0O000O0OOOO00O} file (y/n)? ")).lower ()#line:41
    if OOOOOO000O0O0OO00 =="y":#line:43
        remove_old_file (file_path =O0O00OOO0000O0000 )#line:44
        print (f"Successfully removes {OOO0O000O0OOOO00O}")#line:45
    else :#line:46
        pass #line:47
if __name__ =="__main__":#line:50
    main ()#line:51
