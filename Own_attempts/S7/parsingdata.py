#!/bin/python3

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as bs

url = "" #insert the url here
response = urllib.request.urlopen(url) #get response from url
content = response.read() # read the response
soup = bs(content, 'html.parser') # put the response in a soup object
print(soup.prettify()) #