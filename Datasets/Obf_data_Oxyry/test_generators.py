""#line:12
import random #line:14
def lottery ():#line:17
    ""#line:23
    for _OO000OOO0O0OOOOOO in range (3 ):#line:26
        yield random .randint (1 ,10 )#line:27
    yield random .randint (10 ,20 )#line:30
def test_generators ():#line:33
    ""#line:34
    for O0OOO0OOO0OOOOOOO ,O0000OOOO0O00O0O0 in enumerate (lottery ()):#line:35
        if O0OOO0OOO0OOOOOOO <3 :#line:36
            assert 0 <=O0000OOOO0O00O0O0 <=10 #line:37
        else :#line:38
            assert 10 <=O0000OOOO0O00O0O0 <=20 #line:39
