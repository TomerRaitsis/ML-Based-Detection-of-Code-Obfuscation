import pyttsx3 #line:1
import PyPDF2 #line:2
from tkinter import filedialog #line:3
location =filedialog .askopenfilename ()#line:5
full_text =""#line:6
with open (location ,'rb')as book :#line:8
	try :#line:10
		reader =PyPDF2 .PdfFileReader (book )#line:11
		audio =pyttsx3 .init ()#line:13
		print ('\n')#line:15
		print ('Recommended Speed ------> 115')#line:16
		set_speed =input ('Please Enter Your Prefered Reading Speed --------> ')#line:18
		audio .setProperty ('rate',int (set_speed ))#line:19
		total_pages =reader .numPages #line:21
		print ('\n')#line:23
		print ('Location of File  -------> '+location )#line:24
		print ('\n')#line:25
		print ('Total Number of Pages -------> '+str (total_pages ))#line:26
		try :#line:28
			for page in range (total_pages ):#line:29
				next_page =reader .getPage (page )#line:30
				content =next_page .extractText ()#line:31
				full_text +=content #line:32
			audio .save_to_file (full_text ,'output.mp3')#line:34
			print ("Converting... \n Please Wait....")#line:35
			audio .runAndWait ()#line:36
		except :#line:38
			print ('Task Failed Successfully! ')#line:39
	except :#line:41
		print ('\n')#line:42
		print ('---------> Cannot Read PDF <---------')#line:43
		print ('\n')#line:44
		print ('--------->Invalid PDF format <--------')#line:45
		print ('\n')#line:46
		print ('OR maybe there is something wrong with your brain that you are trying \n to convert a file that is not in .pdf format')