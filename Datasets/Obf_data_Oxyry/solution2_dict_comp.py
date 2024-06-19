#!/usr/bin/env python3
""#line:2
import argparse #line:4
def get_args ():#line:8
    ""#line:9
    OO0O00O0OO0OOO000 =argparse .ArgumentParser (description ='Gashlycrumb',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:13
    OO0O00O0OO0OOO000 .add_argument ('letter',help ='Letter(s)',metavar ='letter',nargs ='+',type =str )#line:19
    OO0O00O0OO0OOO000 .add_argument ('-f','--file',help ='Input file',metavar ='FILE',type =argparse .FileType ('r'),default ='gashlycrumb.txt')#line:26
    return OO0O00O0OO0OOO000 .parse_args ()#line:28
def main ():#line:32
    ""#line:33
    O0OOO00OOOOO0O000 =get_args ()#line:35
    O0O00O0OOO0OOO0O0 ={O0O00000O0OO00000 [0 ].upper ():O0O00000O0OO00000 .rstrip ()for O0O00000O0OO00000 in O0OOO00OOOOO0O000 .file }#line:36
    for OOO0000O0O0OO0OOO in O0OOO00OOOOO0O000 .letter :#line:38
        if OOO0000O0O0OO0OOO .upper ()in O0O00O0OOO0OOO0O0 :#line:39
            print (O0O00O0OOO0OOO0O0 [OOO0000O0O0OO0OOO .upper ()])#line:40
        else :#line:41
            print (f'I do not know "{OOO0000O0O0OO0OOO}".')#line:42
if __name__ =='__main__':#line:46
    main ()#line:47
