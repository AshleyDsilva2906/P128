import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(START_URL)
soup=bs(page.text,"html.parser")
startable=soup.find_all("table")

templist=[]

table_rows=startable[7].find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    templist.append(row)

starnames=[]
distance=[]
mass=[]
radius=[]

for i in range(1,len(templist)):
    starnames.append(templist[i][0])
    distance.append(templist[i][5])
    mass.append(templist[i][7])
    radius.append(templist[i][8])

df2=pd.DataFrame(list(zip(starnames,distance,mass,radius)),columns=["star_name","distance","mass","radius"])
print(df2)
df2.to_csv("dwarf_stars.csv")