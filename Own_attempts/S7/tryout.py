import urllib.request
import urllib.parse
import os 
from bs4 import BeautifulSoup


url = "https://waarnemingen.be"
headers = {}
headers ['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
data_content = response.read()
print(data_content)