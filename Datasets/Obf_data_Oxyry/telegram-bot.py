import os #line:1
from dotenv import load_dotenv #line:2
from chatbot import LLMPromptTemplate #line:3
import telebot #line:4
from notion import createPage #line:8
load_dotenv ()#line:10
BOT_TOKEN =os .getenv ("BOT_TOKEN")#line:12
bot =telebot .TeleBot (BOT_TOKEN )#line:15
@bot .message_handler (commands =["start","hello"])#line:18
def send_welcome (OOOO000OO0O00O0OO ):#line:19
    bot .reply_to (OOOO000OO0O00O0OO ,"Howdy, how are you doing?")#line:20
@bot .message_handler (commands =["Notion"])#line:30
def notion (O00O000000OO000OO ):#line:31
    OOO0OOO000OO0O0OO ="split differnet data with *,*"#line:33
    O0OOO00O0O0O0OOO0 =bot .send_message (O00O000000OO000OO .chat .id ,OOO0OOO000OO0O0OO ,parse_mode ="Markdown")#line:35
    bot .register_next_step_handler (O0OOO00O0O0O0OOO0 ,AddNotion )#line:36
def AddNotion (O00OO0O000000000O ):#line:39
    O00OO0O000000000O =O00OO0O000000000O .text #line:42
    OOOO0O0OOO0O000OO =LLMPromptTemplate (O00OO0O000000000O ,1 )#line:45
    OOO00O00OO000OO00 =LLMPromptTemplate (O00OO0O000000000O ,2 )#line:46
    O00OO0O000000000O =createPage (OOOO0O0OOO0O000OO ,OOO00O00OO000OO00 )#line:48
bot .infinity_polling ()#line:51
