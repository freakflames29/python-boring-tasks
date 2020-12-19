import bs4 , requests

res = requests.get("https://www.flipkart.com/think-like-monk/p/itm7aa0c08edb6a1?pid=9780008386597&lid=LSTBOK9780008386597YY5U4Y&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_3_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_6_na_na_na&fm=SEARCH&iid=f6d3ced5-6277-4d4d-a006-f256ea03b775.9780008386597.SEARCH&ppt=sp&ppn=sp&ssid=2y2s1pryl4mwh91c1608385562491&qH=39a956a2f3581bed")

if res.status_code!=200:
    print("Error connecting")
else:
    content=res.content
# print(content)
soup = bs4.BeautifulSoup(content,"html.parser")
title = soup.select(".B_NuCI")
res = title[0].text.strip()
print("The book name is: "+res)
price = soup.select("._16Jk6d")
priceResult=price[0].text.strip()
print("Price is : "+priceResult)

# res=soup.find(class_="B_NuCI")
# print(res.text)