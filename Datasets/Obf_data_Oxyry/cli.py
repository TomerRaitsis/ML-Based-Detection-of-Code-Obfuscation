import re #line:1
import click #line:3
from proxytest import add_from_text_file #line:5
from proxytest import test_csv_file #line:6
from proxytest import test_single_proxy #line:7
def validate_proxy (OOO00O000O0O0O000 ,O0000O0000O0O00O0 ,OOO0000O0O0O0O00O ):#line:10
    ""#line:11
    O0O00O0O00OOO00OO =re .compile (r'(https|http|socks4|socks5):\/\/' r'((?:[0-9]{1,3}\.){3}[0-9]{1,3}(:[0-9]{2,5})?' r'|([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?)')#line:14
    if not O0O00O0O00OOO00OO .match (OOO0000O0O0O0O00O ):#line:16
        raise click .BadParameter ('Please provide a proxy in the format' 'type://address (e.g., https://42.42.42.42)')#line:18
    else :#line:19
        return OOO0000O0O0O0O00O #line:20
@click .group ()#line:23
def cli ():#line:24
    pass #line:25
@cli .command ()#line:28
@click .argument ('proxy',callback =validate_proxy )#line:29
@click .option ('--iptest',default ='iptest.ingokleiber.de',help ='iptest address')#line:31
@click .option ('--csv',default ='proxies.csv',help ='CSV path')#line:32
def single (OO0O0OOOO0OOO0OOO ,O0000OOO000O0000O ,O0OO00OOO00OO0OOO ):#line:33
    test_single_proxy (OO0O0OOOO0OOO0OOO ,O0000OOO000O0000O ,O0OO00OOO00OO0OOO )#line:34
@cli .command ()#line:37
@click .argument ('csv')#line:38
@click .option ('--iptest',default ='iptest.ingokleiber.de',help ='iptest address')#line:40
def csv_file (O0OOOO00O0OO00000 ,O0OO0OOOO00O00O0O ):#line:41
    test_csv_file (O0OOOO00O0OO00000 ,O0OO0OOOO00O00O0O )#line:42
@cli .command ()#line:45
@click .argument ('txt')#line:46
@click .option ('--iptest',default ='iptest.ingokleiber.de',help ='iptest address')#line:48
@click .option ('--csv',default ='proxies.csv',help ='CSV path')#line:49
def add_from_txt_file (O0OOO00OOO000O000 ,O0OOOO0OOO00O0000 ,OOO0OO00OOO0O0OOO ):#line:50
    add_from_text_file (O0OOO00OOO000O000 ,O0OOOO0OOO00O0000 ,OOO0OO00OOO0O0OOO )#line:51
if __name__ =='__main__':#line:54
    cli ()#line:55
