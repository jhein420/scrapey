import requests
from bs4 import BeautifulSoup

#GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

#parse html
soup = BeautifulSoup(r.content,'html.parser')

#extract image information
images_list = []

images = soup.select('img')

for image in images:
    src = image.get('src' )
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})

for iamge in images_list:
    print(image)