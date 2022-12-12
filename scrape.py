from bs4 import BeautifulSoup
import pandas as pd
list_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
import requests

fettcheddata=requests.get(list_url)
soup=BeautifulSoup(fettcheddata.text,"html.parcel")
req=soup.find("table")
tablerows=req.find_all("tr")
tablercol=req.find_all("tc")
temp_list=[]
for tr in tablerows:
    td=tr.find_all("td")
    row=[i.text.rstrip()
    for i in td:
        temp_list.append(row)]
name=[]
distance=[]
mass=[]
radius=[]

for i in range(1,len(temp_list)):
    name.append(temp_list[i][0])
    distance.append(temp_list[i][1])
    mass.append(temp_list[i][2])
    radius.append(temp_list[i][3])
df=pd.DataFrame(list(name,distance,mass,radius),columns=["NAME","DISTANCE","MASS","RADIUS"])
df.to_csv("starspro.csv")





    
    
    



