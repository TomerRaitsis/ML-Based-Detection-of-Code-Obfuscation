""#line:6
import math #line:8
import random #line:9
import statistics #line:10
def test_math ():#line:13
    ""#line:17
    assert math .cos (math .pi /4 )==0.70710678118654757 #line:18
    assert math .log (1024 ,2 )==10.0 #line:19
def test_random ():#line:22
    ""#line:26
    OOO0O00OO0OOOOO0O =['apple','pear','banana']#line:29
    O00O00OO0OO0O0OO0 =random .choice (OOO0O00OO0OOOOO0O )#line:30
    assert O00O00OO0OO0O0OO0 in OOO0O00OO0OOOOO0O #line:31
    O0000000O0OOOO0O0 =random .sample (range (100 ),10 )#line:34
    for OO0O0OO0000O0O0O0 in O0000000O0OOOO0O0 :#line:35
        assert 0 <=OO0O0OO0000O0O0O0 <=100 #line:36
    OO0O0O0O0O00OO0O0 =random .random ()#line:39
    assert 0 <=OO0O0O0O0O00OO0O0 <=1 #line:40
    OOOO0OO0OO00OOO0O =random .randrange (6 )#line:43
    assert 0 <=OOOO0OO0OO00OOO0O <=6 #line:44
def test_statistics ():#line:47
    ""#line:52
    OO00O0OOO00O00OO0 =[2.75 ,1.75 ,1.25 ,0.25 ,0.5 ,1.25 ,3.5 ]#line:54
    assert statistics .mean (OO00O0OOO00O00OO0 )==1.6071428571428572 #line:56
    assert statistics .median (OO00O0OOO00O00OO0 )==1.25 #line:57
    assert statistics .variance (OO00O0OOO00O00OO0 )==1.3720238095238095 #line:58
