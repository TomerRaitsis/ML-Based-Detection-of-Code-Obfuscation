from constants import GameSettings ,Direction ,Point #line:1
class Snake :#line:4
    ""#line:5
    def __init__ (OOO0O0OO0000OO00O ,init_length =3 ):#line:7
        ""#line:12
        OOO0O0OO0000OO00O .head =Point (GameSettings .WIDTH /2 ,GameSettings .HEIGHT /2 )#line:13
        OOO0O0OO0000OO00O .block_size =GameSettings .BLOCK_SIZE #line:14
        OOO0O0OO0000OO00O .blocks =[OOO0O0OO0000OO00O .head ]+[Point (OOO0O0OO0000OO00O .head .x -(OOOOOOO0OOO0O0OO0 *OOO0O0OO0000OO00O .block_size ),OOO0O0OO0000OO00O .head .y )for OOOOOOO0OOO0O0OO0 in range (1 ,init_length )]#line:18
        OOO0O0OO0000OO00O .direction =Direction .RIGHT #line:19
    def move (OO000O0000OOO00OO ,OO00O0O0O0O00O00O ):#line:21
        ""#line:29
        O0O0OOO00OO0OOO00 ,OOO000O0O0OO0O00O =OO000O0000OOO00OO .head #line:30
        if OO00O0O0O0O00O00O ==Direction .RIGHT :#line:31
            O0O0OOO00OO0OOO00 +=OO000O0000OOO00OO .block_size #line:32
        elif OO00O0O0O0O00O00O ==Direction .LEFT :#line:33
            O0O0OOO00OO0OOO00 -=OO000O0000OOO00OO .block_size #line:34
        elif OO00O0O0O0O00O00O ==Direction .DOWN :#line:35
            OOO000O0O0OO0O00O +=OO000O0000OOO00OO .block_size #line:36
        elif OO00O0O0O0O00O00O ==Direction .UP :#line:37
            OOO000O0O0OO0O00O -=OO000O0000OOO00OO .block_size #line:38
        OO000O0000OOO00OO .head =Point (O0O0OOO00OO0OOO00 ,OOO000O0O0OO0O00O )#line:39
        OO000O0000OOO00OO .blocks .insert (0 ,OO000O0000OOO00OO .head )#line:40
        return OO000O0000OOO00OO .head #line:41
    def self_collision (O0OOO0OO0O000OOOO ):#line:43
        ""#line:48
        if O0OOO0OO0O000OOOO .head in O0OOO0OO0O000OOOO .blocks [1 :]:#line:49
            return True #line:50
        return False #line:51
