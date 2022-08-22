import requests
#requests module

#GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

#print url
#print status code
#print content
print(r.status_code)
print(r.url)
print(r.content)
print('test')