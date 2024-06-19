#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
import re #line:6
def get_args ():#line:10
    ""#line:11
    O0O00000O00000000 =argparse .ArgumentParser (description ='Southern fry text',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:15
    O0O00000O00000000 .add_argument ('text',metavar ='text',help ='Input text or file')#line:17
    O0OO0000O0000O00O =O0O00000O00000000 .parse_args ()#line:19
    if os .path .isfile (O0OO0000O0000O00O .text ):#line:21
        O0OO0000O0000O00O .text =open (O0OO0000O0000O00O .text ).read ()#line:22
    return O0OO0000O0000O00O #line:24
def main ():#line:28
    ""#line:29
    O00OOOO00000O0OOO =get_args ()#line:31
    for O0O00OO0O0O00OO00 in O00OOOO00000O0OOO .text .splitlines ():#line:33
        print (''.join (map (fry ,re .split (r'(\W+)',O0O00OO0O0O00OO00 .rstrip ()))))#line:34
def fry (O0O0OO00O000OOOO0 ):#line:38
    ""#line:39
    if O0O0OO00O000OOOO0 .lower ()=='you':#line:41
        return O0O0OO00O000OOOO0 [0 ]+"'all"#line:42
    if O0O0OO00O000OOOO0 .endswith ('ing'):#line:44
        if any (map (lambda O0O0O0000OO0000OO :O0O0O0000OO0000OO .lower ()in 'aeiouy',O0O0OO00O000OOOO0 [:-3 ])):#line:45
            return O0O0OO00O000OOOO0 [:-1 ]+"'"#line:46
    return O0O0OO00O000OOOO0 #line:48
def test_fry ():#line:52
    ""#line:53
    assert fry ('you')=="y'all"#line:55
    assert fry ('You')=="Y'all"#line:56
    assert fry ('your')=='your'#line:57
    assert fry ('fishing')=="fishin'"#line:58
    assert fry ('Aching')=="Achin'"#line:59
    assert fry ('swing')=="swing"#line:60
if __name__ =='__main__':#line:64
    main ()#line:65
