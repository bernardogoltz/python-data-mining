# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:38:27 2022

@author: bernardogoltz
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs 


# requesting the page and download the html. 
url = 'https://www.pythonscraping.com/pages/warandpeace.html'
html = urlopen(url)

# making the soup
soup = bs(html,'html.parser')

nameList = soup.findAll('span' , {'class':'green'})
# bs.find_all(tagName, tagAttributes)

for item in nameList:
    print(item.get_text())
    
    """ 
    get_text() should always be the last thing you do, immediately 
    before you print, store, or manipulate your final data.
    """
    
name_list_prince_count = len(soup.find_all(text = 'the prince'))

