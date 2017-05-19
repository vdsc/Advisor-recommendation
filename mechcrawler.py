from bs4 import BeautifulSoup
from collections import Counter
from urllib import urlopen
import requests
import urllib
import numpy
import json
import os
import re

y = [] #to store all the links

os.getenv('PORT', '8080')
os.getenv('IP', '0.0.0.0')
url = 'www.me.udel.edu/people/index.html'
# raw_input("enter the web site to extract the url from:")
r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data, "html5lib")
soup.prettify()

div = soup.find('div',attrs={"class":"post"})

for tr in div.find_all('tr'):
    td = tr.find('td')
    if td:
        for link in td.find_all("a"):
            if(link.get('href')):
                href = link.get('href')
                # print href
                if 'http' in href:
                    y.append(href)
                else:
                    y.append(str('http://www.me.udel.edu/people/'+ link.get('href')))

# print y

# now we go inside the links
for i in y:
    try:
        page_content = urlopen(i) 
    except:
        pass
    # parsed_url = urlparse(x[1])
    content = BeautifulSoup(page_content.read(), "html5lib")
    content.prettify()
    
    
    div = content.find('div',{"class" : "post" })
    # print div
    name = div.find('h2').get_text()
    
    email = div.find('p').find('a')['href']
    # print email
    website = i
    # print website
    text = ''
    for raw in  div.find_all('p'): 
        print raw.contents
    
    # print text
    print '---'
    
    
    