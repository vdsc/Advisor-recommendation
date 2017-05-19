from bs4 import BeautifulSoup
import os
import requests
import urllib2
# import lxml.html
from urllib import urlopen
from urlparse import urlparse

import json


print os.environ["PORT"]
print os.environ["IP"]

x =  [] #to store all prof links here
url = raw_input("Enter a website to extract the URL's from: ")

# def get_data(prof_link):
#     r  = requests.get(url)

#     data = r.text

#     soup = BeautifulSoup(data)
#     soup.prettify()
#      for tag in soup.findAll('p'):

r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html5lib")
soup.prettify()

for link in soup.find_all(['a'], {'class':'info'}):
    if(link.get('href')):
        x.append(str('http://www.ece.udel.edu'+ link.get('href')))
        # print('http://www.ece.udel.edu'+ link.get('href'))
# for a in x:
#     print(a)
#     get_data(a)
#     # prof_links.append()
page_content = urlopen(x[2])
parsed_url = urlparse(x[2])


beautiful_content = BeautifulSoup(page_content.read(), "html5lib")

beautiful_content.prettify()

# print beautiful_content
# for strong_tag in beautiful_content.find_all('strong'):
#      print strong_tag.text, strong_tag.next_sibling
     
for node in beautiful_content.findAll(['p','h2']):
     print ''.join(node.findAll(text=True))
   

    
    



    


    
    
    

