from sys import path_hooks
from turtle import clear
from types import new_class
from bs4 import BeautifulSoup
from operator import is_not
from functools import partial
import numpy as np
import requests, openpyxl,re,pathlib
import pandas as pd
import os

def function(base,first,i):
    excel = openpyxl.Workbook()
    sheet = excel.active    
    sheet.title = "Chapters"
    i = str(i)
    sheet.title  = sheet.title + i
    print(excel.sheetnames)
    print(excel)
    url = base+first
    print("Inside function")
    print(url)
    source = requests.get(url)
    source.raise_for_status()
    soup = BeautifulSoup(source.text,'html.parser')
    
    if soup.find("span",class_="mw-page-title-main"):
        heading = soup.find("span",class_="mw-page-title-main")
        print("Yes")
    else:
        return
    heading = heading.text
    print(type(heading))
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
    file_name = "Dataset"
    file_name = file_name+i
    extension = ".xlsx"
    file_name = file_name+extension
    print(file_name)
    excel.save(file_name)
    return file_name


base = "https://en.wikipedia.org"
path_of_file = os.getcwd()
newPath = path_of_file.replace(os.sep, '/')
newPath = newPath + '/'
directory_path = newPath
first ="/wiki/React_(JavaScript_library)"
file_name = function(base,first,0)
newPath = newPath + file_name
print(newPath)
df = pd.DataFrame(pd.read_excel(newPath))

#df.filter(like ='#')
#print(df)
#df.to_excel('raw_data.xlsx')
df = df.T
i = 1
paths = []
for row in (df.items()):
    if i<3:
        x = row[1]
        df1 = x.to_frame().T
        f = df1.to_string(header=False,index=False).replace(" ","")
        path = function(base,f,i)
        paths.append(path)
    else:
        break
    i=i+1  

paths = list(filter(None, paths))
newPath = path_of_file.replace(os.sep, '/')
i=i+1
for j in range(len(paths)):
    if i<100:
        newPath = paths[j]
        print(newPath)
        df = pd.DataFrame(pd.read_excel(newPath))
        df = df.T
        for row in (df.items()):
            x = row[1]
            df1 = x.to_frame().T
            f = df1.to_string(header=False,index=False).replace("c ","")
            path = function(base,f,i)
            paths.append(path)
            i=i+1 