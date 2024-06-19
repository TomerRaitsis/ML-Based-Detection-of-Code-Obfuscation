#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
import re #line:6
def get_args ():#line:10
    ""#line:11
    OO0OO0OO0OO0OOO00 =argparse .ArgumentParser (description ='Apples and bananas',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:15
    OO0OO0OO0OO0OOO00 .add_argument ('text',metavar ='text',help ='Input text or file')#line:17
    OO0OO0OO0OO0OOO00 .add_argument ('-v','--vowel',help ='The vowel to substitute',metavar ='vowel',type =str ,default ='a',choices =list ('aeiou'))#line:25
    OOOOO0O0O000OO0O0 =OO0OO0OO0OO0OOO00 .parse_args ()#line:27
    if os .path .isfile (OOOOO0O0O000OO0O0 .text ):#line:29
        OOOOO0O0O000OO0O0 .text =open (OOOOO0O0O000OO0O0 .text ).read ().rstrip ()#line:30
    return OOOOO0O0O000OO0O0 #line:32
def main ():#line:36
    ""#line:37
    OOOO00O0O0O0OO0O0 =get_args ()#line:39
    OO000O0OOOOOO0O0O =OOOO00O0O0O0OO0O0 .vowel #line:40
    O00000O00OO0O00O0 =str .maketrans ('aeiouAEIOU',OO000O0OOOOOO0O0O *5 +OO000O0OOOOOO0O0O .upper ()*5 )#line:41
    O0OO0O00O000OO000 =OOOO00O0O0O0OO0O0 .text .translate (O00000O00OO0O00O0 )#line:42
    print (O0OO0O00O000OO000 )#line:44
if __name__ =='__main__':#line:48
    main ()#line:49
