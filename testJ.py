from bs4 import BeautifulSoup
import os
import requests
import urllib2
# import lxml.html
from urllib import urlopen
from urlparse import urlparse


print os.environ["PORT"]
print os.environ["IP"]

x =  [] #to store all prof links here
#url = raw_input("Enter a website to extract the URL's from: ")
url = 'http://www.cis.udel.edu/people/index.html'

# def crawlSite(self, linksList):
#     finalList = []
#     for link in list(linksList):
#         if link not in finalList:
#             print link            
#             finalList.append(link)
#             childLinks = self.getAllUniqueLinks(link)
#             length = len(childLinks)
#             print 'Total links for this page: ' + str(length)

#         self.crawlSite(childLinks)
#     return finalList

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)
soup.prettify()

for link in soup.find_all('a', {'class':'info'}):
    if(link.get('href')):
        x.append(str('http://www.cis.udel.edu'+ link.get('href')))
        # print('http://www.cis.udel.edu'+ link.get('href'))

print x[0]


page_content = urlopen(x[0])
parsed_url = urlparse(x[0])

beautiful_content = BeautifulSoup(page_content.read())
beautiful_content.prettify()
# print beautiful_content
# for strong_tag in beautiful_content.find_all('strong'):
#      print strong_tag.text, strong_tag.next_sibling
     
for node in beautiful_content.findAll('p'):
    print ''.join(node.findAll(text=True))





		


    # k  = requests.get(x[0])
    # d = k.text
    # soup = BeautifulSoup(d)
    # soup.prettify()
    # print soup.body

 


    
    
    

