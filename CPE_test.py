#!/usr/bin/env python
# coding: utf-8

# In[29]:


import requests
import re
import os
from bs4 import BeautifulSoup
# global
Path = "C:\\Users\\USER\\Desktop\\cpeTest"
path_list = []
URL = 'https://cpe.cse.nsysu.edu.tw/history.php'
HTML = requests.get(URL)
SP = BeautifulSoup(HTML.text, 'html5lib')
regex_date = r'(\d{4})/(\d{2})/(\d{2})'
regex_pdf = r'\s*(\d*): \w*'
file_index=0
# make outer dir
if not os.path.isdir(Path):
    os.mkdir(Path)
# make dir name = date
for a in SP.find_all('td'):
    date = re.match(regex_date,a.text)
    if date:
        name = date.group(1) + "." + date.group(2) + "." + date.group(3)
        if name=="2021.05.25":
            continue
        path = Path + "\\" + name
        if not os.path.isdir(path):
            os.mkdir(path)
            print("creating dir: %s"%name)
        path_list.append(path)
# download pdf
for a in SP.find_all('a'):
    if a.text == "考試題目":
        url = a['href']
        html = requests.get(url)
        sp = BeautifulSoup(html.text, 'html5lib')
        print("open file: %s",path_list[file_index])
        for b in sp.find_all('a'):
            file = re.match(regex_pdf,b.text)
            if file:
                url = b['href']
                response = requests.get(url)
                with open(path_list[file_index] + "\\" + file.group(1)+".pdf", 'wb') as f:
                    f.write(response.content)
                    print("file.pdf: %s downloading" % file.group(1))
                    f.close()
        file_index+=1


# In[ ]:





# In[ ]:




