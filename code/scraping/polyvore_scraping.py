
# coding: utf-8

# In[9]:

#Libraries Import
from lxml import html
import requests
import pandas as pd
import urllib
from urllib.request import urlopen
import re
from PIL import Image


# In[17]:

#Url connection
url = 'https://www.polyvore.com/what_to_wear/'
html_link = str(urlopen(url).read())
#Pages with sets detection
pages = []
for i in re.finditer('../([A-Za-z0-9_]+)/(set\?id=+)[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',html_link):
    pages.append(url+i.group(0))
pages = list(set(pages))


# In[11]:

#Sets dictionary
set_combo = {}
string = '<img width="600" alt=(.+?) src=(.+?) title=(.+?) id=(.+?) class="main_img" height="600" />'
for link in pages:
    page = requests.get(link)
    tree = html.fromstring(page.content)  
    html_string = str(page.content)
    dresses = []
    for i in re.finditer('"title":("(.+?)")',html_string): dresses.append(i.group(1))
    img_str = re.findall(string, html_string)[0]
    likes = re.findall('class="fav_count">(.+?)<',html_string)[0]
    set_combo[img_str[1]] = [set(dresses),likes,link]


# In[12]:

#Show scraped sets
URL = list(set_combo.keys())
for u in URL:
    with urllib.request.urlopen(u.strip('"')) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())
        img = Image.open('temp.jpg')
        img.show()

