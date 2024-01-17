#!/bin/python3

# ask the user for different kinds of input
# use that input to search and filter this online rescource
# save both photos and metadata locally on your pc

import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as bs
import wget 
import csv

url = 'https://waarnemingen.be'
data_after = input("\nGive date after (in YYYY-MM-DD format): ")
url_photos = url + "/photos/?date_after=" + data_after
date_before = input("\nGive date before (in YYYY-MM-DD format): ")
url_photos = url_photos + "&date_before=" + date_before
