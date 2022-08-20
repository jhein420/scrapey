import requests
from bs4 import BeautifulSoup

#GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

#check status code - 200
print(r)

#parse html
soup = BeautifulSoup(r.content,'html.parser')
print(soup.prettify())