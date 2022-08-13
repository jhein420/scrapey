import requests
from bs4 import BeautifulSoup

#GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

#parse html
soup = BeautifulSoup(r.content,'html.parser')

s = soup.find('div', class_='entry-content')
 
lines = s.find_all('p')

#show text in tags
for line in lines:
    print(line.text)