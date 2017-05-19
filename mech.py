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


div = soup.find('div', {'class':'post'})
# for link in soup.select('strong a'):
for link in div.find_all('strong a'):
    #if(link.get('href')):
        y.append(str('http://www.me.udel.edu/people/'+ link.get('href')))
        print(link.get('href'))
        
print (y)