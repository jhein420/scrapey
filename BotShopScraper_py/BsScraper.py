#scraper for https://botshop.co.za/ using beautiful soup
#getting product details
import requests
from bs4 import BeautifulSoup
import csv

def main():
    #functions
    prep()

#functions for scraping
def prep():
    url = 'https://botshop.co.za/collections/all'
    r= requests.get(url)

    soup = BeautifulSoup(r.content,'html.parser')
    tag = 'main'
    att = ''
    cl = 'main-content'
    i = ''
    print(r.status_code)
    #getProductUrlDetails(tag, cl, i, soup, att)
    getProductDetails(tag, cl, soup)

#gets name , price and details of products
def getProductDetails(tag, cl, sp):
    s = sp.find(tag,class_= cl)
    ProductNamelist = []
    ProductPriceList = []
    for link in s.find_all('a',class_='product-title'):
        #print(link.span.text)
        ProductNamelist.append(link.span.text)
    
    for li in s.find_all('div',class_='price-regular'):
        ProductPriceList.append(li.span.text)
    
    prodToCsv(ProductNamelist, ProductPriceList)
            
            

#get product URls and details
def getProductUrlDetails( tag, cl, idn, sp, att):
    s = sp.find(tag, class_= cl)
    lines = s.find_all('a')
    for line in lines:
        print(line.get(att))

#take scraped product details and put them into a csv
def prodToCsv(pN, pp):
    productList = []
    count = 0
    for p in pN:
        d = {}
        d['Name'] = pN[count]
        d['Price'] = pp[count]
        count+=1
        productList.append(d)
    
    filename = 'productDetails.csv'
    with open(filename,'w', newline='') as f:
        w = csv.DictWriter(f,['Name', 'Price'])
        w.writeheader()
        w.writerows(productList)

if __name__ == "__main__":
    main()