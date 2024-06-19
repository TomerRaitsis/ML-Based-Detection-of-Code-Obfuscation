#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
def get_args ():#line:9
    ""#line:10
    O00O0O0000O000000 =argparse .ArgumentParser (description ='Apples and bananas',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:14
    O00O0O0000O000000 .add_argument ('text',metavar ='text',help ='Input text or file')#line:16
    O00O0O0000O000000 .add_argument ('-v','--vowel',help ='The vowel to substitute',metavar ='vowel',type =str ,default ='a',choices =list ('aeiou'))#line:24
    OO00O00O0000OO0O0 =O00O0O0000O000000 .parse_args ()#line:26
    if os .path .isfile (OO00O00O0000OO0O0 .text ):#line:28
        OO00O00O0000OO0O0 .text =open (OO00O00O0000OO0O0 .text ).read ().rstrip ()#line:29
    return OO00O00O0000OO0O0 #line:31
def main ():#line:35
    ""#line:36
    OOOO0OOO0O0O000OO =get_args ()#line:38
    OOO000OOO0O0O0O0O =OOOO0OOO0O0O000OO .text #line:39
    O00OOOO000OO00OOO =OOOO0OOO0O0O000OO .vowel #line:40
    O00O0OOOO0OO0OOOO =[]#line:41
    for OOOO00OO000000OO0 in OOO000OOO0O0O0O0O :#line:43
        if OOOO00OO000000OO0 in 'aeiou':#line:44
            O00O0OOOO0OO0OOOO .append (O00OOOO000OO00OOO )#line:45
        elif OOOO00OO000000OO0 in 'AEIOU':#line:46
            O00O0OOOO0OO0OOOO .append (O00OOOO000OO00OOO .upper ())#line:47
        else :#line:48
            O00O0OOOO0OO0OOOO .append (OOOO00OO000000OO0 )#line:49
    print (''.join (O00O0OOOO0OO0OOOO ))#line:51
if __name__ =='__main__':#line:55
    main ()#line:56
