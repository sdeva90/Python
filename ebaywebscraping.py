import csv
import urllib.request
from bs4 import BeautifulSoup
f = open('edata.csv', 'w', newline='')
writer = csv.writer(f)
# data = []
soup = BeautifulSoup(urllib.request.urlopen("http://www.ebay.com/sch/i.html?_from=R40&_trksid=p2050601.m570.l1311.R5.TR12.TRC2.A0.H0.Xpixhawk.TRS0&_nkw=pixhawk+flight+controller&_sacat=0").read(), 'lxml')
gdata = soup.find_all("li", {"class": "sresult lvresult clearfix li shic"}, limit = 1)
for child in gdata:
    itemname = child.find_all('h3', {"class": "lvtitle"})
    itemname = [ele.text.strip() for ele in itemname]
    ul = child.findChildren("ul")
    print(itemname)
    for price in ul:
        w = price.findChildren('li', {"class": "lvprice prc"})
        w = [ele.text.strip() for ele in w]
        if w :
            print(w)
            break
    for sold in ul:
        s = sold.findChildren('div', {"class": "hotness-signal red"})
        s = [ele.text.strip() for ele in s]
        if s:
            print(s)
            break
    # writer.writerow(itemname, w, s)
        print(data)
    # print(ul)
# print(gdata.encode("utf-8"))
# print(gdata.decode('utf-8').encode('cp850','replace').decode('cp850'))
# for item in gdata:
#     print(item.contents[0])
# cols = [ele.text.strip() for ele in cols]
