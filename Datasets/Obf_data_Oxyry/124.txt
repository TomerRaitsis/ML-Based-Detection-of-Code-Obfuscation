#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
import re #line:6
def get_args ():#line:10
    ""#line:11
    OOO0000O000O000O0 =argparse .ArgumentParser (description ='Apples and bananas',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:15
    OOO0000O000O000O0 .add_argument ('text',metavar ='text',help ='Input text or file')#line:17
    OOO0000O000O000O0 .add_argument ('-v','--vowel',help ='The vowel to substitute',metavar ='vowel',type =str ,default ='a',choices =list ('aeiou'))#line:25
    O0O000O0OO0000OOO =OOO0000O000O000O0 .parse_args ()#line:27
    if os .path .isfile (O0O000O0OO0000OOO .text ):#line:29
        O0O000O0OO0000OOO .text =open (O0O000O0OO0000OOO .text ).read ().rstrip ()#line:30
    return O0O000O0OO0000OOO #line:32
def main ():#line:36
    ""#line:37
    OOOO00OOO0O00O00O =get_args ()#line:39
    OOOO0OO00000OO000 =OOOO00OOO0O00O00O .text #line:40
    OO00OOOOO00000OO0 =OOOO00OOO0O00O00O .vowel #line:41
    for OO0O00OO0OOO0O00O in 'aeiou':#line:43
        OOOO0OO00000OO000 =OOOO0OO00000OO000 .replace (OO0O00OO0OOO0O00O ,OO00OOOOO00000OO0 ).replace (OO0O00OO0OOO0O00O .upper (),OO00OOOOO00000OO0 .upper ())#line:44
    print (OOOO0OO00000OO000 )#line:46
if __name__ =='__main__':#line:50
    main ()#line:51
