import urllib2  
from bs4 import BeautifulSoup
import os
import requests



print os.environ["PORT"]
print os.environ["IP"]



from datetime import datetime  
  
quote_page = 'http://www.bloomberg.com/quote/SPGSCITR:IND'  

t1 = datetime.now()

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_store = soup.find('h1', attrs={'div' : 'name'})   

data_name = name_store.text.strip()  
 
price_store = soup.find('div', attrs={'class': 'price'})

price = price_store.text
  
print data_name     

t2 = datetime.now() 

total = t2 -t1 

print 'scraping completed in ' ,  total