import time #line:1
import pyautogui #line:3
def send_message (OOO00OOO0OO0OOOO0 ,O0O00000O00OO0O0O ):#line:6
    ""#line:13
    try :#line:14
        print ("5 seconds to navigate to slack app..")#line:15
        time .sleep (5 )#line:16
        pyautogui .hotkey ("command","k")#line:19
        time .sleep (1 )#line:20
        pyautogui .typewrite (OOO00OOO0OO0OOOO0 )#line:22
        time .sleep (1 )#line:23
        pyautogui .typewrite (["enter"])#line:24
        time .sleep (1 )#line:25
        O00OOOOO0O0OO000O =pyautogui .locateOnScreen ("active_identifier.png")#line:27
        if not O00OOOOO0O0OO000O :#line:29
            print (f"{OOO00OOO0OO0OOOO0} is not active, skipped contact")#line:30
            return #line:31
        print ("Contact is active, sending message...")#line:33
        pyautogui .typewrite (["tab"])#line:34
        pyautogui .typewrite (O0O00000O00OO0O0O )#line:35
        pyautogui .typewrite (["enter"])#line:36
    except KeyboardInterrupt :#line:38
        print ("Process was cancelled..")#line:39
if __name__ =="__main__":#line:42
    contacts =input ("Enter contact list, separated by space >> Messi Onazi John: ").split (" ")#line:46
    message =input ("Enter the message you wish to send out to them: ")#line:47
    for c in contacts :#line:49
        contact =c .strip ()#line:50
        send_message (contact ,message )#line:51
