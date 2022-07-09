import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
import pandas as pd


start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"  
page=requests.get(start_url)
print(page)

soup=bs(page.text,'html.parser')
star_table=soup.find('table')
templist=[]
table_rows=star_table.find_all("tr")
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    templist.append(row)
star_names=[]
distance=[]
mass=[]
radius=[]
lum=[]
for i in range (1,len(templist)):
    star_names.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    lum.append(templist[i][7])

df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity']   ) 
df2.to_csv("bright_stars.csv")