# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:28:07 2022

@author: bernardogoltz
b.

"""

from urllib.request import urlopen
from urllib.error import HTTPError

from bs4 import BeautifulSoup 

def getTitle(url):
    
    try:
        html = urlopen(url)
        
    except HTTPError as e:
        return None 
    
    try: 
        soup = BeautifulSoup(html, 'html.parser')
        
        title = soup.body.h1.get_text()

    except AttributeError as e:
        return None
    
    return title 

url = 'https://www.pythonscraping.com/pages/page1.html'

title = getTitle(url)

if title == None: 
    print('For some reason, title could not be found')
    
else:
    print("The title is:  {}".format(title))
    


