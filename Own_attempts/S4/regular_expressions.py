#!/bin/python3

import re

text = "A big black bug bit a big black dog on his big black nose"
checktext = re.compile('bi.', re.IGNORECASE)
matches = checktext.findall(text)
print(matches)

findall = re.findall('.i.', text)
print(findall)

findall2 = re.findall('\s\w\w\w\s', text)
print(findall2)

replace = re.sub('ig', 'ag', text)
print(replace)

search = re.search('bit', text)
print(search)
