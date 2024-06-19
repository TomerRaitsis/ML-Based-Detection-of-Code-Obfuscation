from unittest .mock import patch #line:1
from calculate_age import age_calculator #line:2
@patch ("time.time",return_value =1621848668.0 )#line:5
def test_age_calculator (OOOOOO00OOO00O0O0 ):#line:6
    ""#line:11
    O0OO00O0000OO0000 ="Chloe"#line:12
    O00O0OOOO000OOO00 =30 #line:13
    OO0O00OOOO0000000 ="Chloe's age is 30 years or 365 months or 11102 days"#line:14
    assert age_calculator (O0OO00O0000OO0000 ,O00O0OOOO000OOO00 )==OO0O00OOOO0000000 #line:15
def test_age_calculator_negative_age ():#line:18
    ""#line:22
    OOO000OO0O0OO0OO0 ="Emma"#line:23
    O0OOOO00OO0000000 =-5 #line:24
    try :#line:25
        age_calculator (OOO000OO0O0OO0OO0 ,O0OOOO00OO0000000 )#line:26
    except ValueError as O0O0OO0O00O0OO000 :#line:27
        assert str (O0O0OO0O00O0OO000 )=="Please input a positive number."#line:28
@patch ("time.time",return_value =1621848668.0 )#line:31
def test_age_calculator_leap_year (OOOO000O000OO000O ):#line:32
    ""#line:36
    O0OO0O0O00OO0OOO0 ="David"#line:37
    O0OOOOOOOOO0O00O0 =30 #line:38
    OO000O000O0OOO0O0 ="David's age is 30 years or 365 months or 11102 days"#line:39
    assert age_calculator (O0OO0O0O00OO0OOO0 ,O0OOOOOOOOO0O00O0 )==OO000O000O0OOO0O0 #line:40
