#!/bin/python3

import urllib.request
import urllib.parse

url = 'https://tryphp.w3schools.com/demo/demo_form_validation_complete.php'
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"

# Empty the file
open('/home/guest/_repos/savefile.txt', 'w').close()

params = {
    'name':'Test',
    'email':'test@gmail.com',
    'website':'www.howest.be',
    'comment':'nothing',
    'gender':'other',
}

query = urllib.parse.urlencode(params)
data = query.encode("utf-8")

try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(url, data)
    #respone_data = response.read()
    response_data = response.read().decode('utf-8')
    print(response_data)
    save_file = open('/home/guest/_repos/savefile.txt', 'w')
    save_file.write(str(response_data))
    save_file.close()
except Exception as e:
    print(str(e))