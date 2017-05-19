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

#print os.environ["PORT"
#print os.environ["IP"]
x =  [] #to store all prof links here
url = "http://www.ece.udel.edu/people/faculty.php"

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

professors = []
for i in x[:]:
    # print i
    try:
        page_content = urlopen(i)
    except:
        pass
    # parsed_url = urlparse(x[1])
    beautiful_content = BeautifulSoup(page_content.read(), "html5lib")
    beautiful_content.prettify()
    
    # print beautiful_content
    # for strong_tag in beautiful_content.find_all('strong'):
    #      print strong_tag.text, strong_tag.next_sibling

    
    professor = {}
    
    for div in beautiful_content.find_all('div', {"class" : "post"}):
        # for name in div.find("h2"):
            # print name
        name = div.find("h2")
        if(name):
            print name.get_text()
            Name = name.get_text()
        for link in div.findAll('p', href=True, text='website'):
            site = link['href']
            print link.find_next_siblings
            print site
            # print raw
        for link in div.findAll('a', href=True, text='email'):
            email = link['href']
            print email
            
    # for node in div.findAll(['p','h2']):
    #     try:
    #         raw += ''.join(node.findAll(text=True))
    #         print raw
    #     except:
    #         pass
            
        
        # for link in div.find('p'):
        # try:
        #     raw = div.find_all("p").get_text()
        #     print raw
        # except: pass
        # raw = div.find_all('p')[6]
        
        
        
    
    # try:.
    #     name = beautiful_content.find("div",{"class":"post"}).find_all("h2").get_text()
    # except:
    #     pass
    
    raw = ''
    for node in beautiful_content.findAll(['p','h2']):
        try:     
             raw += ''.join(node.findAll(text=True))
             print raw
        except:
            pass
    #     try:
    #         email = beautiful_content.find("div",{"id":"faculty-right"}).find_all("a")[0].attrs['href']
    #     except:
    #         pass
    #     try:    
    #         site = beautiful_content.find("div",{"id":"faculty-right"}).find_all("a")[1].attrs['href']
    #     except:
    #         pass
        
    professor['raw'] = raw
    
    professor['email'] = email
    
    professor['site'] = i
    
    professor['name'] = Name
    
    # print professor
    professors.append(professor)
    # print Counter(raw.split()).most_common()
# print professors
    
    # test = json.dumps(professors)
    #print email
     #print site

# with open('test.json','w') as fp:
#     json.dump(professors,fp,indent=4)
# print test