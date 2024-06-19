import sys #line:1
import os #line:2
from Cryptodome .Cipher import AES #line:3
from Cryptodome import Random #line:4
from binascii import b2a_hex #line:5
def encrypt_dir (OOOOOOO0O0OO000O0 ):#line:8
    for O00O00OO00OOOO00O ,_OO00OO0OO00OO0OOO ,OO000000O00O00OO0 in os .walk ("."):#line:9
        for OO00O0O00O00000O0 in OO000000O00O00OO0 :#line:10
            O0O00OO0OO0O00O0O =os .path .join (O00O00OO00OOOO00O ,OO00O0O00O00000O0 )#line:11
            print (O0O00OO0OO0O00O0O +" is encrypting.")#line:12
            encrypt_file (O0O00OO0OO0O00O0O )#line:13
def encrypt_file (OO00000OO0O0OO000 ):#line:16
    with open (OO00000OO0O0OO000 )as OOOO0OOO000O00O0O :#line:18
        O0O000O0O0OO00O0O =OOOO0OOO000O00O0O .read ()#line:19
    O00OO00OOOOO00O00 =b'this is a 16 key'#line:22
    O0O0OO000OO00000O =Random .new ().read (AES .block_size )#line:24
    OOOOOO0OOOOO0O000 =AES .new (O00OO00OOOOO00O00 ,AES .MODE_CFB ,O0O0OO000OO00000O )#line:25
    OO00OOO0O0OO0O00O =O0O0OO000OO00000O +OOOOOO0OOOOO0O000 .encrypt (O0O000O0O0OO00O0O .encode ())#line:26
    with open (OO00000OO0O0OO000 +".bin","wb")as O00OO00OOOO00OOO0 :#line:29
        O00OO00OOOO00OOO0 .write (OO00OOO0O0OO0O00O [16 :])#line:30
path =sys .argv [1 ]#line:33
if os .path .isdir (path )and os .path .exists (path ):#line:34
    encrypt_dir (path )#line:35
elif os .path .isfile (path )and os .path .exists (path ):#line:36
    encrypt_file (path )#line:37
else :#line:38
    print ("it's a special file(socket,FIFO,device file)")#line:39
