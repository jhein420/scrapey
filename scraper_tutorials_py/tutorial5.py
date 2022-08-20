import requests
from bs4 import BeautifulSoup

#GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

#parse html
soup = BeautifulSoup(r.content,'html.parser')

#find all anchor tags with 'href'
for link in soup.find_all('a'):
    print(link.get('href'))