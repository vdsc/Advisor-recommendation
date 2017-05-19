from collections import Counter
from bs4 import BeautifulSoup
import os
import requests
import urllib2
# import lxml.html
from urllib import urlopen
from urlparse import urlparse
import numpy
import itertools

import json

# http://www.cis.upenn.edu/about-people/


x =  [] #to store all prof links here
#url = raw_input("Enter a website to extract the URL's from: ")
os.getenv('PORT', '8080')
os.getenv('IP', '0.0.0.0')
url = 'http://www.cis.upenn.edu/about-people/'


r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html5lib")
soup.prettify()

unicode = "\u00a0"
y = []

# table = soup.find('table').find_all("tr")
# print table

# for row in table.findAll(('tr')[1]):
#     for row1 in row.find('td'):
#         print row1
#         print '----------'
professors = []
x = []
y =[]
count =0
countweb = 0
countprof =0
# for row in soup.findAll('table')[0].tbody.findAll('tr'):
#     # try:
#     #     first_column = row.findAll('td')[0].contents
#     #     print first_column
#     # except: 
#     #     pass
#     try: 
#         prof = row.findAll('td')[1]
        
#         for link in prof.findAll('a', href=True, text='Website'):
#             x.append(link['href'])
        
         
#         # print prof
#         count +=1
        
#     except: pass
for row in soup.findAll('table')[0].tbody.findAll('tr'):
    # try:
    #     first_column = row.findAll('td')[0].contents
    #     print first_column
    # except: 
    #     pass
    try: 
        # prof = row.findAll('td')[1]
        # print prof
        
        for link in row.findAll('a', text='View Profile'):
            if(link['href']):
                x.append(link['href'])
            else:
                x.append('null')
            # countweb += 1;
        # for link in row.findAll('a', text='View Profile'):
        #     if(link['href']):
        #         y.append(link['href']) 
        #     else:
        #         y.append('null')
        #     countprof += 1
        
         
        # print prof
        count +=1
        
    except: pass
# for i in x:
#     print i

for i in x[:]:
    # print i
    professor = {}
    try:
        page_content = urlopen(i)
    except:
        pass
    # parsed_url = urlparse(x[1])
    soup = BeautifulSoup(page_content.read(), "html5lib")
    soup.prettify()
    div = soup.find('div',attrs={"class":"mainContent"})
    # print div
    for link in div.findAll('a', href=True, text='Email'): 
        email = link['href']
        # print email
    # for link in div.find('h1'): 
    #     Name = link.get_text()
    for link in div.findAll('a', href=True, text='Personal Webpage'): 
        webpage = link['href']
        # print webpage
    for link in div.findAll('h1'): 
        if link:
            name = link.get_text()
            
            # name = name.text.replace(/\u00a0, " ");
            
            
            # name.replace('\u00a0', ' ')
    profdata = div.find_all('p', {'class': 'mainContent'})[2].contents
    profdata = (", ".join(profdata))
     
    # print profdata
    professor['raw'] = profdata   
    professor['email'] = email
        
    professor['site'] = webpage
    professor['name'] = name
    
    professors.append(professor)
    
print professors


with open('upenn.json','w') as fp:
    json.dump(professors,fp,indent=4)
# third_paragraph = div.find_all('p')
# print third_paragraph
