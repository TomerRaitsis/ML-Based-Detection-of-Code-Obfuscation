import requests #line:1
import os #line:2
from datetime import datetime ,timezone #line:3
from dotenv import load_dotenv #line:4
load_dotenv ()#line:6
import json #line:7
from datetime import datetime ,timezone #line:8
token =os .getenv ("NOTION_TOKEN")#line:11
dataset =os .getenv ("DATABASE_ID")#line:12
headers ={"Authorization":"Bearer "+token ,"Content-Type":"application/json","Notion-Version":"2022-02-22",}#line:18
def createPage (O00O0OOOO000OO0OO ,OOOO000OO00O0OO0O ):#line:22
    OOOO0O00O00O0OOOO ="https://api.notion.com/v1/pages"#line:23
    OO0000OOOO000O00O ={"parent":{"database_id":dataset },"properties":{"Descriptions":{"id":"title","type":"title","title":[{"type":"text","text":{"content":O00O0OOOO000OO0OO ,},}],},"Youtube URL":{"url":OOOO000OO00O0OO0O },},}#line:41
    OO0O0000O00OOO0O0 =json .dumps (OO0000OOOO000O00O )#line:42
    OO0O0O0O0O00OO0OO =requests .request ("POST",OOOO0O00O00O0OOOO ,headers =headers ,data =OO0O0000O00OOO0O0 )#line:43
    print (OO0O0O0O0O00OO0OO .status_code )#line:44
    if OO0O0O0O0O00OO0OO .status_code ==200 :#line:45
        return True #line:46
    else :#line:47
        False #line:48
