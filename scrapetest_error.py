from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
  try:
    bsObj= BeautifulSoup(html.read(),'lxml')
    title= bsObj.body.h1
  except AttributeError as e:
    return None
  return title
title=getTitle("https://github.com/Manojpesarlanka/python-web-scraping/edit/main/scrapetest_error.py.html")
if title == None:
  print("Title is not found")
else:
  print(title)
  
  
