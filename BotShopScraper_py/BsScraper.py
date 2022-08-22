#scraper for https://botshop.co.za/ using beautiful soup
import requests
from bs4 import bs

url = 'https://botshop.co.za/collections/all'
r= requests.get(url)

soup = bs(r.content,'html.parser')
tag = 'a'
att = 'href'

for link in soup.find_all(tag):
    print(link.get(att))