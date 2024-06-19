from turtle import *#line:1
import turtle as t #line:2
import random #line:3
import time #line:4
tim =t .Turtle ()#line:6
t .colormode (255 )#line:8
def random_colour ():#line:11
    O0OO0OO0OOOOOOOO0 =random .randint (0 ,255 )#line:12
    O0O0O0000O0000O00 =random .randint (0 ,255 )#line:13
    O00OOOO0OOOO00OOO =random .randint (0 ,255 )#line:14
    return O0OO0OO0OOOOOOOO0 ,O0O0O0000O0000O00 ,O00OOOO0OOOO00OOO #line:16
def turtle_movement ():#line:19
    tim .pensize (10 )#line:20
    O0OOO000O0000OO0O =random_colour ()#line:21
    OOO0OOOO0OO0O0000 =random .randint (1 ,4 )#line:22
    tim .pencolor (O0OOO000O0000OO0O [0 ],O0OOO000O0000OO0O [1 ],O0OOO000O0000OO0O [2 ])#line:23
    if OOO0OOOO0OO0O0000 ==1 :#line:25
        tim .left (90 )#line:26
        tim .forward (30 )#line:27
        time .sleep (0.5 )#line:28
    elif OOO0OOOO0OO0O0000 ==2 :#line:29
        tim .right (90 )#line:30
        tim .forward (30 )#line:31
        time .sleep (0.5 )#line:32
    elif OOO0OOOO0OO0O0000 ==3 :#line:33
        tim .forward (30 )#line:34
        time .sleep (0.5 )#line:35
    elif OOO0OOOO0OO0O0000 ==4 :#line:36
        tim .backward (30 )#line:37
        time .sleep (0.5 )#line:38
colours =["GreenYellow","Chartreuse","Tan","LightSkyBlue","DeepPink","MediumSlateBlue",]#line:48
t .pensize (10 )#line:50
for _ in range (0 ,200 ):#line:51
    turtle_movement ()#line:52
screen =Screen ()#line:54
screen .exitonclick ()#line:55
