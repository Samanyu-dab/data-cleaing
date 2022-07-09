
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.by import By

start_url="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"  
browser=webdriver.Chrome("F:\c127\chromedriver.exe")
browser.get(start_url)
time.sleep(10)

planet_data=[]

headers=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date","hyperlink"]
def scrape():
    headers=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data=[]
    for i in range(0,505):
        soup=BeautifulSoup(browser.page_source)
        for ul_tag in soup.find_all("ul",attrs={"class","expo planet"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate("li_tags"):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.content[0])
                    except:temp_list.append("")
            hyperlink_li_tag=li_tags[0]
            temp_list.append("https://exoplanets.nasa.gov"+ hyperlink_li_tag.find_all("a", href=True)[0]["href"])        
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()        
        print(f"page{i} scraping completed")   
    with open("scrapper_2.csv","w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)        
        csvwriter.writerows(planet_data)
scrape()        

new_planets_data=[]
def scrape_more_data(hyperlink):
    try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content,"html.parser")
        temp_list=[]
        for tr_tag in soup.find_all("tr",attrs={"class":"fact_row"}):
            td_tags=tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_planet_data.append(temp_list)
    except:
        time.sleep(10)
        scrape_more_data(hyperlink)   

for index,data in enumerate(planet_data):
    scrape_more_data(data[5])
    print(f"scrapping at hyperlink{index+1} is completed")
 
print(new_planets_data[0:10])
final_planet_data=[]
for index,data in enumerate(planet_data):
    new_planets_data_element=new_planets_data(index)
    new_planets_data_element=[elem.replace("\n","")for elem in new_planets_data_element]
    new_planets_data_element=new_planets_data_element[:7]
    final_planet_data.append(data+new_planets_data_element)

with open("final.csv","w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)        
        csvwriter.writerows(final_planet_data)
    
