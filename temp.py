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
import wikipedia as wiki

base_url = "https://en.wikipedia.org"
first_url ="/wiki/React_(JavaScript_library)"
url = base_url+first_url
print(url)
source = requests.get(url)
source.raise_for_status()
soup = BeautifulSoup(source.text,'html.parser')    
if soup.find("span",class_="mw-page-title-main"):
    heading = soup.find("span",class_="mw-page-title-main")
    #print("Yes")
topics = []
heading = heading.text
summary = wiki.summary(heading)
topics.append(heading)
topics.append(summary)
for tag in soup.select('p a[title]'):      
    topic = tag['title']
    topics.append(topic)
excel = openpyxl.Workbook()
sheet = excel.active    
sheet.title = "Chapters"
#print(topics)
new_df = pd.DataFrame(data=topics)
print(new_df)

sheet.append(topics)
file_name = "Dataset"
extension = ".xlsx"
file_name = file_name+extension
print(file_name)
excel.save(file_name)
    