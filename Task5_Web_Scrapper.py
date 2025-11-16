import requests
from bs4 import BeautifulSoup
import csv
url1 = "https://books.toscrape.com/"
page1 = requests.get(url1)
soup1 = BeautifulSoup(page1.text,"html.parser")
items1 = soup1.find_all("article", class_="product_pod")
data1 = []
for x1 in items1:
    name1 = x1.h3.a["title"]
    price1 = x1.find("p", class_="price_color").text
    rate1 = x1.p["class"][1]
    data2 = [name1, price1, rate1]
    data1.append(data2)
f1 = open("products.csv","w",newline="")
w1 = csv.writer(f1)
w1.writerow(["name","price","rating"])
for d1 in data1:
    w1.writerow(d1)
f1.close()
print("done")