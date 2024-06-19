from random import randint #line:5
class Jogadores :#line:8
    nome :str #line:9
    cartas =[]#line:10
    def __init__ (OO00OOO000OOOOOO0 ,O00O0OO0O000OO0OO ):#line:12
        OO00OOO000OOOOOO0 .nome =O00O0OO0O000OO0OO #line:13
        OO00OOO000OOOOOO0 .cartas =[]#line:14
    def distribuir_cartas (O0OO0O00OOOO00O00 )->list :#line:17
        for OO00OO0O00O0OO00O in range (3 ):#line:18
            OO0OO00OOO000OO0O =randint (1 ,3 )#line:19
            O0OO0O00OOOO00O00 .cartas .append (OO0OO00OOO000OO0O )#line:20
        return O0OO0O00OOOO00O00 .cartas #line:21
    def traduzir_cartas (O0OO00OO0OO00O0O0 ,OOO000O00OOOO00OO )->list :#line:24
        OO00O0OO00OO000OO =""#line:25
        for O00O0O0OO0O0OOOOO in OOO000O00OOOO00OO :#line:26
            if O00O0O0OO0O0OOOOO ==1 or O00O0O0OO0O0OOOOO =="1":#line:27
                OO00O0OO00OO000OO +="Stone "#line:28
            elif O00O0O0OO0O0OOOOO ==2 or O00O0O0OO0O0OOOOO =="2":#line:29
                OO00O0OO00OO000OO +="Paper "#line:30
            else :#line:31
                OO00O0OO00OO000OO +="Scissors "#line:32
        return OO00O0OO00OO000OO #line:34
    def limpar_cartas (O00O00000OO0OO00O ):#line:37
        return O00O00000OO0OO00O .cartas .clear ()#line:38
