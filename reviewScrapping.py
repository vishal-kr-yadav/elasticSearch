import urllib2
from bs4 import BeautifulSoup
import requests
import pandas as pd
import unicodedata
import re
from connection import createDocument
from connection import executeQuery
# def scrappingReviewFromAmazon():

list = []
res = requests.get("https://www.amazon.in/Apple-iPhone-Space-Grey-256GB/dp/B072LNNSQN/ref=sr_1_4?s=electronics&ie=UTF8&qid=1519143645&sr=1-4&keywords=iphone+x&dpID=41wUnHPGFBL&preST=_SY300_QL70_&dpSrc=srch")
soup = BeautifulSoup(res.content, 'lxml')
for each in soup.find_all('div',attrs={'class':'a-section review'}):
    reviewData = unicodedata.normalize('NFKD', re.sub('\s+', ' ', each.text)).encode('ascii', 'ignore').split(':')
    list.append(reviewData[0])
    # print("in for")
print(list[0])
    # executeQuery()


# scrappingReviewFromAmazon()
# print(type(result))
# print(result)
