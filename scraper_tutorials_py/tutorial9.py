import requests
from bs4 import bs
import csv

#saving to a csv file example

URL = 'https://www.geeksforgeeks.org/page/'
req = requests.get(URL)
soup = bs(req.text, 'html.parser')

#save titles to csv
titles = soup.find_all('div', attrs={'class','head'})
titles_list = []

count = 1

for title in titles:
    d = {}
    d['Title Number']= f'Title {count}'
    d['Title Name'] = title.text
    count+=1
    titles_list.append(d)

filename = 'titles.csv'
with open(filename,'w', newline='') as f:
    w = csv.DictWriter(f,['Title Number', 'Title Name'])
    w.writeheader()
    w.writerows(titles_list)