from urllib.request import urlopen
html=urlopen("http://github.com/Manojpesarlanka/python-web-scraping/new/main.html")
print(html.read())

#so here it scraping this page, & gets all the html tags, textile heads and body
