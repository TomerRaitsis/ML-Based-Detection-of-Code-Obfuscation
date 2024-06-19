#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
def get_args ():#line:9
    ""#line:10
    O00OOOOOOO0OOOOOO =argparse .ArgumentParser (description ='Apples and bananas',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:14
    O00OOOOOOO0OOOOOO .add_argument ('text',metavar ='text',help ='Input text or file')#line:16
    O00OOOOOOO0OOOOOO .add_argument ('-v','--vowel',help ='The vowel to substitute',metavar ='vowel',type =str ,default ='a',choices =list ('aeiou'))#line:24
    OO00O0OOO00O0O00O =O00OOOOOOO0OOOOOO .parse_args ()#line:26
    if os .path .isfile (OO00O0OOO00O0O00O .text ):#line:28
        OO00O0OOO00O0O00O .text =open (OO00O0OOO00O0O00O .text ).read ().rstrip ()#line:29
    return OO00O0OOO00O0O00O #line:31
def main ():#line:35
    ""#line:36
    OO000O00OOOOO0O0O =get_args ()#line:38
    O000O0OO000O000OO =OO000O00OOOOO0O0O .vowel #line:39
    def OO00OO00OO0O0OO0O (OO00OO000O0000OO0 ):#line:41
        return O000O0OO000O000OO if OO00OO000O0000OO0 in 'aeiou'else O000O0OO000O000OO .upper ()if OO00OO000O0000OO0 in 'AEIOU'else OO00OO000O0000OO0 #line:42
    print (''.join (map (OO00OO00OO0O0OO0O ,OO000O00OOOOO0O0O .text )))#line:44
if __name__ =='__main__':#line:48
    main ()#line:49
