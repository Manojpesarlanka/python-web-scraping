from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
    html = urlopen("https://github.com/Manojpesarlanka/python-web-scraping/new/main.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print("the server could not be found")
else:
    print("it worked")
