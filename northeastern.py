from collections import Counter
from bs4 import BeautifulSoup
import os
import requests
import urllib2
# import lxml.html
from urllib import urlopen
from urlparse import urlparse
import numpy

import json

#print os.environ["PORT"]
#print os.environ["IP"]

x =  [] #to store all prof links here
url = 'http://www.ccis.northeastern.edu/people-view-all/'
# http://www.ccis.northeastern.edu/people-view-all/


r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html5lib")
soup.prettify()
# print soup


body = soup.find("div", {'class':'grid-item'}).get_text()




# for link in div.find_all('a'):
#     if(link.get('href')):
#         # y.append(str('http://www.me.udel.edu/people/'+ link.get('href')))
#         print(link.get('href'))