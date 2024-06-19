#!/usr/bin/env python3
""#line:2
import argparse #line:4
import re #line:5
import sys #line:6
def get_args ():#line:10
    ""#line:11
    OOOOOO0O000O0OO0O =argparse .ArgumentParser (description ='Mad Libs',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:15
    OOOOOO0O000O0OO0O .add_argument ('file',metavar ='FILE',type =argparse .FileType ('rt'),help ='Input file')#line:20
    OOOOOO0O000O0OO0O .add_argument ('-i','--inputs',help ='Inputs (for testing)',metavar ='input',type =str ,nargs ='*')#line:27
    return OOOOOO0O000O0OO0O .parse_args ()#line:29
def main ():#line:33
    ""#line:34
    O0O0OOO0O000O00O0 =get_args ()#line:36
    OO00O0O000000OO0O =O0O0OOO0O000O00O0 .inputs #line:37
    OOOOOO0O00OOO0O0O =O0O0OOO0O000O00O0 .file .read ().rstrip ()#line:38
    O00000OOOO0OO0000 =re .findall ('(<([^<>]+)>)',OOOOOO0O00OOO0O0O )#line:39
    if not O00000OOOO0OO0000 :#line:41
        sys .exit (f'"{O0O0OOO0O000O00O0.file.name}" has no placeholders.')#line:42
    O0O0OO00O00OO0OOO ='Give me {} {}: '#line:44
    for O000O0OOO000O000O ,OOO0O00OO0000000O in O00000OOOO0OO0000 :#line:45
        O0O00O000O0O00OO0 ='an'if OOO0O00OO0000000O .lower ()[0 ]in 'aeiou'else 'a'#line:46
        O0O0OOOO00O000OOO =OO00O0O000000OO0O .pop (0 )if OO00O0O000000OO0O else input (O0O0OO00O00OO0OOO .format (O0O00O000O0O00OO0 ,OOO0O00OO0000000O ))#line:47
        OOOOOO0O00OOO0O0O =re .sub (O000O0OOO000O000O ,O0O0OOOO00O000OOO ,OOOOOO0O00OOO0O0O ,count =1 )#line:48
    print (OOOOOO0O00OOO0O0O )#line:50
if __name__ =='__main__':#line:54
    main ()#line:55
