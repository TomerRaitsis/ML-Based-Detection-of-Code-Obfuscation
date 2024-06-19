from hashlib import sha256 #line:1
import time #line:2
MAX_NONCE =100000000000 #line:5
def SHA256 (OOO0OOO0O00OO0O00 ):#line:11
    return sha256 (OOO0OOO0O00OO0O00 .encode ("ascii")).hexdigest ()#line:12
def mine (OO0O00O0OO0O00000 ,OO0O000OOO0OO00OO ,OOO0OO0OO0OO0O000 ,O0O0O0OO0O00000OO ):#line:18
    O0000OOO000O0O00O ="0"*O0O0O0OO0O00000OO #line:19
    for OO0OO00O00O0OOOOO in range (MAX_NONCE ):#line:20
        OOO0OOOOOOO0O0O0O =str (OO0O00O0OO0O00000 )+OO0O000OOO0OO00OO +OOO0OO0OO0OO0O000 +str (OO0OO00O00O0OOOOO )#line:21
        O0O000OO0OOO0OO00 =SHA256 (OOO0OOOOOOO0O0O0O )#line:22
        if O0O000OO0OOO0OO00 .startswith (O0000OOO000O0O00O ):#line:23
            print (f"Yay! Successfully mined bitcoins with nonce value:{OO0OO00O00O0OOOOO}")#line:24
            return O0O000OO0OOO0OO00 #line:25
    raise BaseException (f"Couldn't find correct has after trying {MAX_NONCE} times")#line:27
if __name__ =="__main__":#line:30
    transactions ="""
    Player1->Player2->200,
    Player3->Player4->450
    """#line:34
    difficulty =6 #line:35
    start =time .time ()#line:39
    print ("start mining")#line:40
    new_hash =mine (5 ,transactions ,"0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7",difficulty ,)#line:46
    total_time =str ((time .time ()-start ))#line:47
    print (f"end mining. Mining took: {total_time} seconds")#line:48
    print (new_hash )#line:49
