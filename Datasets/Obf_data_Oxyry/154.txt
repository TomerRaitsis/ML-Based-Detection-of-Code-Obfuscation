import yt_dlp #line:1
def download_youtube_video (O0O0O000OOO000OOO ):#line:4
    ""#line:5
    O00OO0OOOO0O0OO0O ={"outtmpl":"%(title)s.%(ext)s",}#line:9
    with yt_dlp .YoutubeDL (O00OO0OOOO0O0OO0O )as O00000OO0OOO0O000 :#line:10
        OOO0O000O000OO0OO =O00000OO0OOO0O000 .extract_info (O0O0O000OOO000OOO ,download =False )#line:11
        O00O0OO0O0OOO0OO0 =OOO0O000O000OO0OO .get ("formats",None )#line:12
        for O0O0OO0O00O000O0O in O00O0OO0O0OOO0OO0 :#line:15
            print (f"{O0O0OO0O00O000O0O['format_id']}:\t{O0O0OO0O00O000O0O['ext']} ({O0O0OO0O00O000O0O.get('format_note', None)}p)")#line:16
        OO0O0OO0O00000O0O =input ("Do you want to select from the available options? (y/n): ")#line:20
        if OO0O0OO0O00000O0O .lower ()=="y":#line:22
            OO000OOOO0O00OO0O =input ("Enter the format id of the video: ")#line:23
            O00OO0OOOO0O0OO0O ["format"]=OO000OOOO0O00OO0O #line:24
        else :#line:25
            OOO0O0OO0OO0O0OO0 =max (O00O0OO0O0OOO0OO0 ,key =lambda O0OO0OOO0OO0O0O00 :O0OO0OOO0OO0O0O00 .get ("height",0 ))#line:27
            OO000OOOO0O00OO0O =OOO0O0OO0OO0O0OO0 ["format_id"]#line:28
            O00OO0OOOO0O0OO0O ["format"]=OO000OOOO0O00OO0O #line:29
        O00000OO0OOO0O000 .download ([O0O0O000OOO000OOO ])#line:32
        print ("Download complete using yt-dlp!")#line:33
if __name__ =="__main__":#line:36
    video_url =input ("Enter the URL: ")#line:37
    download_youtube_video (video_url )#line:38
