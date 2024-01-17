#!/usr/bin/python3

from bs4 import BeautifulSoup
import os
import urllib.request
import urllib.parse 

#define the url and the headers
url = ("https://www.google.com/") #change the url here
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"



# Empty the file
open('/home/guest/_repos/savefile.txt', 'w').close()

#try out and catch errors + write to the file
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    print(response_data)
    save_file = open('/home/guest/_repos/savefile.txt', 'w')  # Open the file in write mode
    save_file.write(str(response_data))
    save_file.close()
except Exception as e:
    print(str(e))