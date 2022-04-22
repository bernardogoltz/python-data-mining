# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:15:45 2022

@author: bernardogoltz

"""

import requests
from bs4 import BeautifulSoup

url  = "https://www.newegg.com/p/2SN-0001-01SH6"

result = requests.get(url)

doc = BeautifulSoup(result.text , "html.parser")


prices = doc.find_all(text = "$")

parent = prices[0].parent
strong = parent.find("strong")

price = strong.string
print("The Price is ${}".format(price))

price = float(price.replace(',' , '.'))
print(round(price*1.10,2))


