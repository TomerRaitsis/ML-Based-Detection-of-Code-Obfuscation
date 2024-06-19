from ursina import *#line:1
class Test_cube (Entity ):#line:5
    def __init__ (OOO0OO00O0O00OO0O ):#line:6
        super ().__init__ (parent =scene ,model ="cube",texture ="white_cube",rotation =Vec3 (45 ,45 ,45 ))#line:9
class Test_button (Button ):#line:13
    def __init__ (OO0O0O00O0O0OO0O0 ,scale =0.1 ):#line:14
        super ().__init__ (parent =scene ,model ="cube",texture ="brick",color =color .white ,highlight_color =color .red ,pressed_color =color .lime ,)#line:22
    def input (O00OOO000O0O0O000 ,O00OO0000000O0O00 ):#line:24
        if O00OOO000O0O0O000 .hovered :#line:25
            if O00OO0000000O0O00 =="left mouse down":#line:26
                punch_sound .play ()#line:27
def update ():#line:31
    if held_keys ["a"]:#line:33
        cube .x -=1 *time .dt #line:34
app =Ursina ()#line:38
cube =Entity (model ="quad",color =color .orange ,scale =(2 ,5 ),position =(5 ,1 ))#line:41
test =Test_cube ()#line:49
btn =Test_button ()#line:52
punch_sound =Audio ("assets/punch",loop =False ,autoplay =False )#line:53
app .run ()#line:55
