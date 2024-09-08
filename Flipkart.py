from bs4 import BeautifulSoup as bs
import requests
import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017")
db1 = db["Flipkart"]

LINKS = []
PRODUCT_NAME = []
PRICE = []
RATING = []
SPECIFICATION_R = []

search = input("Enter the Product : ")
coll = db1[search]

# only for no of pages
url = f"https://www.flipkart.com/search?q={search}"
web = requests.get(url).text
s = bs(web, "html.parser")
no_of_pages = int(s.find("div", class_="_2MImiq").find("span").text.split()[-1].replace(",", "_"))
for page_no in range(1, no_of_pages+1):
    try:
        URL = f"https://www.flipkart.com/search?q={search}&page={page_no}"
        webpage = requests.get(URL).text
        scrap = bs(webpage, "html.parser")
        link = scrap.find_all("a", class_="_1fQZEK")
        links_l = [i.get("href") for i in link]
        LINKS.extend(links_l)
    except:
        break

else:
    for each_link in LINKS:
        try:
            URL2 = "https://www.flipkart.com" + each_link
            webpage2 = requests.get(URL2).text
            scrap2 = bs(webpage2, "html.parser")
            PRODUCT_NAME.append(scrap2.find("span", class_="B_NuCI").text.strip())
            PRICE.append(scrap2.find("div", class_="_30jeq3 _16Jk6d").text.strip())
            RATING.append(scrap2.find("div", class_="_3LWZlK").text.strip())
            rating = scrap2.find_all("text", class_="_2Ix0io")
            feature = scrap2.find_all("div", class_="_3npa3F")
            SPECIFICATION_R.append([(i.text.strip(), j.text.strip()) for i, j in zip(feature, rating)])
        except Exception as e:
            print(e)

dic_data = {
    "Product Name": PRODUCT_NAME,
    "Price": PRICE,
    "Rating": RATING,
    "Feature Rating": SPECIFICATION_R
}

coll.insert_one(dic_data)
