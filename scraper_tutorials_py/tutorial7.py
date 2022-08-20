import requests
from bs4 import BeautifulSoup
#Looping through the page numbers
#GET request
url = 'https://www.geeksforgeeks.org/page/'
r = requests.get(url) 

#parse html
#soup = BeautifulSoup(r.content,'html.parser')

#titles = soup.find_all('div', attrs = {'class','head'})

#print(titles[4].text)

for page in range(1,10):
    req = requests.get(url + str(page) + '/')
    soup = BeautifulSoup(req.text,'html.parser')

    titles = soup.find_all('div', attrs = {'class','head'})
    for i in range(4,19):
        if page>1:
            print(f"{(i-3)+page*15}" + titles[i].text)
        else:
            print(f"{i-3}"+ titles[i].text)