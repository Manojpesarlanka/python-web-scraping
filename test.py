import requests
from bs4 import BeautifulSoup
import csv

url="https://www.bikewale.com/royalenfield-bikes/"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')

#images
img1=[]
image=soup.findAll('div',class_="imageWrapper")
for i in image:
    j=i.img['src']
    img1.append(j)
print(img1)
print()
#links
links=[]
link=soup.findAll('div',class_="bikeDescWrapper")
for i in link:
    j=i.a['href']
    links.append(j)
print(links)
print()
links=[]
link=soup.findAll('div',class_="bikeDescWrapper")
for i in link:
    j=i.a.text
    links.append(j)
print(links)

"""with open('imglink.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(image)
    for i in image:
        j=i.img['src']
        img1.append(j)
    write.writerow(img1)"""

with open('bikelink.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(image)
    for i in link:
        j=i.a['href']
        links.append(j)
    write.writerow(links)