from collections import Counter
from bs4 import BeautifulSoup
import os
import requests
import urllib2
from urllib import urlopen
from urlparse import urlparse
import numpy
import itertools
import json
import re

os.getenv('PORT', '8080')
os.getenv('IP', '0.0.0.0')
url = 'http://www.depts.ttu.edu/ece/faculty/'


r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html5lib")
soup.prettify()

raw = ''
final = ''
prof = []
professors = []
temp = ''
#print soup

def get_prof_data(i):
    # print i
    try:
        page_content = urlopen(i) 
    except:
        pass
    # parsed_url = urlparse(x[1])
    content = BeautifulSoup(page_content.read(), "html5lib")
    content.prettify()
    
    div = content.find('div',{"id" : "content" })
    div = div.find('ul').get_text()
    
    
    
    return div

#for link in soup.find_all(['div'], {'id':'faculty'}):
for node in soup.find('table',attrs={"class":"fancy"}):
    
    for link in node.find_all('tr',attrs={"class":"person"}):
        professor = {}
        for email in link.findAll('a', href=True, text='Email'):
            Email = email['href']
        for site in link.findAll('a', href=True, text='Website'):
            try:
                Website = site['href']
            except: pass# print Website
            raw = get_prof_data(Website)
        for name in link.find('td').next_sibling():
            Name = name.get_text()
        
        professor['name'] = Name
        professor['email'] = Email
        professor['site'] = Website
        professor['raw'] = raw
        # print professor
        # raw = get_prof_data(Website)
            # print "-------"
        # for resh in link.findAll('li'):
        #     try:
        #         raw = str(resh.get_text())
        #     except:
        #         pass
        # print raw
            # print "-------"
        # print '--------'
        # professor["name"] = Name
        # professor["email"] = Email
        # professor["site"] = Website
        # professor["raw"] = raw
        # print professor
        professors.append(professor)
# #         # print "-------------------------------"
for i in professors:
    print i
with open('texastech.json','w') as fp:
    json.dump(professors,fp,indent=4)