from asyncore import write
import csv
from email import header

from requests import head

dataset1=[]
dataset2=[]

with open("final.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)
        
    
with open("archive_sorted1.csv","r")as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)
header1=dataset1[0]
planetdata1=dataset1[1:]

header2=dataset2[0]
planetdata2=dataset2[1:]
headers=header1+header2

planetdata=[]

for index,data_row in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])
    
with open("merged_dataset.csv","a+") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planetdata)    
