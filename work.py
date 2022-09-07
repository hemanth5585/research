
from sys import path_hooks
from bs4 import BeautifulSoup
import requests, openpyxl,re,pathlib
import pandas as pd
import os
excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active    
sheet.title = "Chapters"
sheet.append(['sub-topic'])
print(excel)

url = "https://en.wikipedia.org/wiki/React_(JavaScript_library)"
base = "https://en.wikipedia.org"
source = requests.get("https://en.wikipedia.org/wiki/React_(JavaScript_library)")
source.raise_for_status()
soup = BeautifulSoup(source.text,'html.parser')
heading = soup.find("span",class_="mw-page-title-main").text
print(heading)
c = 0
for tag in soup.select('p a[href]'):      
    if c ==0:
        sheet.append([heading])
        c = 1
    topic = tag['href']
    if topic.startswith('#') or topic.startswith('http'):
        a = 0
    else:
        sheet.append([topic])
file_name = "DataSet.xlsx"
excel.save(file_name)

path_of_file = os.getcwd()
newPath = path_of_file.replace(os.sep, '/')
newPath = newPath + '/'
newPath = newPath + file_name

df = pd.DataFrame(pd.read_excel(newPath))
df = df.T
df.filter(like ='#')
print(df)
df.to_excel('raw_data.xlsx')
