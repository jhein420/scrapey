import requests
from bs4 import BeautifulSoup

#GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

#parse html
soup = BeautifulSoup(r.content,'html.parser')

#get title tag, its name and parent tag
print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)

#find by class attribute
s= soup.find('div', class_='entry-content')
content = s.find_all('p')
#print(content)

#find by id
s1 = soup.find('div', id ='main')

#get left bar
leftbar = s1.find('ul', class_='leftBarList')

# All the li under the above ul
content1 = leftbar.find_all('li')
 
print(content1)
