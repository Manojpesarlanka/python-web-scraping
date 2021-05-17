from urllib.request import urlopen
from bs4 import BeautifulSoup
#here bs lib helps messy web by fixing the bad HTML

html = urlopen("https://github.com/Manojpesarlanka/python-web-scraping/new/main.html")

bsObj=BeautifulSoup(html.read(),'lxml')
#we just want to collect one obj from HTML document which have put in bsObj variable


print(bsObj.h1)
#now o/p is loaded into bsObj var & HTML content is transformed into bs4 object with structure
