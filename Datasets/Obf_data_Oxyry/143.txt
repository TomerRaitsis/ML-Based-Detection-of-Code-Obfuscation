""#line:6
import json #line:8
def test_json ():#line:11
    ""#line:12
    OOOO0OO0O0000O0OO ={'first_name':'John','last_name':'Smith','age':42 }#line:20
    assert OOOO0OO0O0000O0OO ['first_name']=='John'#line:21
    assert OOOO0OO0O0000O0OO ['age']==42 #line:22
    O0000OO0000O0O000 ='{"first_name": "John", "last_name": "Smith", "age": 42}'#line:24
    O0O0000000O0OO0OO =json .loads (O0000OO0000O0O000 )#line:28
    assert O0O0000000O0OO0OO ==OOOO0OO0O0000O0OO #line:30
    assert O0O0000000O0OO0OO ['first_name']=='John'#line:31
    assert O0O0000000O0OO0OO ['age']==42 #line:32
    OO0OO0000000OO0O0 =json .dumps (OOOO0OO0O0000O0OO )#line:36
    assert OO0OO0000000OO0O0 ==O0000OO0000O0O000 #line:38
