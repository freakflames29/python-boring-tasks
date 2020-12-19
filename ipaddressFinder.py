import bs4,requests

def ipadd(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    elems = soup.select("body > main:nth-child(1) > div:nth-child(1) > h1:nth-child(1)")
    return elems[0].text.strip()

ipis = ipadd("https://ipecho.net/")
print("Your global ip is "+ipis)
