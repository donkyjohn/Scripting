#!/bin/python3

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as bs

url = "http://www.cazy.org/GH100_all.html" #insert the url here
response = urllib.request.urlopen(url) #get response from url
content = response.read() # read the response
soup = bs(content, 'html.parser') # put the response in a soup object
#print(soup.prettify()) #
'''
#option1 search tagwise
var=soup.find("table", {"class":"listing"})
print(var)
var2=soup.find_all("td", {"id":"separateur2"})
x=1
for td in var2:
    print("[{}] {}".format(x,td))
    print("--> Name = {} | string = {}".format(td.name, td.string))
    x = x+1
'''
'''
#option2 check with descendants
var=soup.find("table",{"class":"listing"})
for child in var.descendants:
    print("NEW CHILD:\n{}".format(child))
'''
'''
#option3 to find the parent/child structure
print("\nParents:")
soup_table=soup.find("table", class_="listing")
for parent in soup_table.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
'''
'''
option_tag = soup.find("option")
for options in option_tag.find_next_sibling():
    print("Next option sibling: {}".format(options))
'''
'''
tr_td_span = soup.select('tr td span')
print("\ntr td span:\n".format(tr_td_span))
'''  