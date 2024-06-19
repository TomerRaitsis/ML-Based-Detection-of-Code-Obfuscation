#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
import re #line:6
def get_args ():#line:10
    ""#line:11
    O0OOOOOO0O0O0O0OO =argparse .ArgumentParser (description ='Apples and bananas',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:15
    O0OOOOOO0O0O0O0OO .add_argument ('text',metavar ='text',help ='Input text or file')#line:17
    O0OOOOOO0O0O0O0OO .add_argument ('-v','--vowel',help ='The vowel to substitute',metavar ='vowel',type =str ,default ='a',choices =list ('aeiou'))#line:25
    OO0OOO0OO0OOO000O =O0OOOOOO0O0O0O0OO .parse_args ()#line:27
    if os .path .isfile (OO0OOO0OO0OOO000O .text ):#line:29
        OO0OOO0OO0OOO000O .text =open (OO0OOO0OO0OOO000O .text ).read ().rstrip ()#line:30
    return OO0OOO0OO0OOO000O #line:32
def main ():#line:36
    ""#line:37
    O0O0OO0000O0O0O00 =get_args ()#line:39
    OO0OO0O0OO00OO000 =O0O0OO0000O0O0O00 .text #line:40
    OOOOOOOO0OO00OOO0 =O0O0OO0000O0O0O00 .vowel #line:41
    OO0OO0O0OO00OO000 =re .sub ('[aeiou]',OOOOOOOO0OO00OOO0 ,OO0OO0O0OO00OO000 )#line:42
    OO0OO0O0OO00OO000 =re .sub ('[AEIOU]',OOOOOOOO0OO00OOO0 .upper (),OO0OO0O0OO00OO000 )#line:43
    print (OO0OO0O0OO00OO000 )#line:44
if __name__ =='__main__':#line:48
    main ()#line:49
