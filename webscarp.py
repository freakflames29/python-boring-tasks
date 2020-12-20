import bs4
import requests
import sys
import pyperclip as pc
# content=''


def getInformaton(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error connecting")
    else:
        content = response.content
    soup = bs4.BeautifulSoup(content, "html.parser")
    NameoftheBook = soup.select(".B_NuCI")
    el = NameoftheBook[0].text.strip()
    itemis=soup.select("div._3GIHBu:nth-child(2) > a:nth-child(1)")
    nameOftheitemis=itemis[0].text.strip()
    print("Item type is:-")
    print("*******************")
    print(nameOftheitemis)
    print("*******************")
    print("The name of the Item is: ")
    print("*******************")
    print(el)
    print("*******************")
    PriceOFtheBook = soup.select("._16Jk6d")
    ElemntPrice = PriceOFtheBook[0].text.strip()
    print("The price of the item is:-")
    print(ElemntPrice)
    print("*******************")
    print("More information about the Item")
    print("*******************")
    BookInformation = soup.select("li._21Ahn-")
    for i in BookInformation:
        print(i.string)
    print("*******************")
    
   

sys.argv
if len(sys.argv) > 1:
    theurlis = sys.argv[1:]
    # url=(r'theurlis')
    url="".join(theurlis)
    
    # print(url)
    getInformaton(url)
else:
    thepaste=pc.paste()
    if thepaste=="":
        print("Enter a url or copy a url")
    else:
        getInformaton(thepaste)
