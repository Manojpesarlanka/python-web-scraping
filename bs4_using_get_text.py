from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj=BeautifulSoup(html,'lxml')
names=bsObj.finAll('spam',{'class':'green'})
for name in names:
  print(name.get_text())
 
#get_text meansGetting just text from websites is a common task. Beautiful Soup provides the method get_text() for this purpose.
#If we want to get only the text of a Beautiful Soup or a Tag object, we can use the get_text() method.
