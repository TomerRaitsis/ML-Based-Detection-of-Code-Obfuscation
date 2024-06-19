from turtle import Turtle #line:1
import random #line:2
COLORS =["red","orange","yellow","green","blue","purple"]#line:4
STARTING_MOVE_DISTANCE =5 #line:5
MOVE_INCREMENT =5 #line:6
class CarManager (Turtle ):#line:11
    def __init__ (O0O000OOOOOO0O000 ):#line:15
        O0O000OOOOOO0O000 .all_cars =[]#line:18
        O0O000OOOOOO0O000 .car_speed =STARTING_MOVE_DISTANCE #line:19
    def create_car (O000000OOO0O0O0O0 ):#line:21
        OO00OOOOOOO0OOOOO =random .randint (1 ,6 )#line:24
        if OO00OOOOOOO0OOOOO ==1 :#line:26
            """
            By this the car will be created only when 1 will come so there will be some distance between the 
            cars where out turtle can move.
            """#line:30
            O0O00OO00O0O00OO0 =Turtle ()#line:33
            O0O00OO00O0O00OO0 .color (random .choice (COLORS ))#line:35
            O0O00OO00O0O00OO0 .shape ("square")#line:36
            O0O00OO00O0O00OO0 .penup ()#line:37
            O0O00OO00O0O00OO0 .shapesize (stretch_wid =1 ,stretch_len =2 )#line:38
            O0O0OOO0O00O00000 =random .randint (-250 ,250 )#line:39
            O0O00OO00O0O00OO0 .goto (300 ,O0O0OOO0O00O00000 )#line:40
            O000000OOO0O0O0O0 .all_cars .append (O0O00OO00O0O00OO0 )#line:41
    def move_car (O00O00OOO0OOO0O00 ):#line:44
        for O0OOO0O00O00O0O0O in O00O00OOO0OOO0O00 .all_cars :#line:47
            O0OOO0O00O00O0O0O .backward (O00O00OOO0OOO0O00 .car_speed )#line:48
    def level_up_speed (OO0000000O00OOO00 ):#line:50
        OO0000000O00OOO00 .car_speed +=MOVE_INCREMENT #line:53
