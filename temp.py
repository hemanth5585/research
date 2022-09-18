from email.mime import base
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
class my_dictionary(dict):

    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


base_url = "https://en.wikipedia.org"
first_url ="/wiki/React_(JavaScript_library)"
url = base_url+first_url
print(url)
source = requests.get(url)
source.raise_for_status()
soup = BeautifulSoup(source.text,'html.parser')    
if soup.find("span",class_="mw-page-title-main"):
    heading = soup.find("span",class_="mw-page-title-main")
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
new_df = pd.DataFrame(data=topics)
#print(new_df)
sheet.append(topics)
file_name = "Dataset"
extension = ".xlsx"
file_name = file_name+extension
print(file_name)
excel.save(file_name)


dict_obj = my_dictionary()
dict_obj1 = my_dictionary()
""" 
dict_obj.add(1, 'Geeks')
dict_obj.add(2, 'forGeeks')

print(dict_obj)

#using dictionaries for second excel
c = 0
for tag in soup.select('p a[title]'):      
    topic = tag['title']
    dict_obj.add(topic,"")
 """
i = 0 
title = ""
for tag in soup.select('p a'):
    topic = tag['href']
    if topic.startswith('#') or topic.startswith('http'):
        a = 0
    else:
        #print(topic)
        reduced_string = re.sub(r'.', '', topic, count = 6)
        result = reduced_string.replace('_', ' ')
        topic = base_url + topic
        dict_obj.add(result,topic)
        dict_obj1.add(result,False)
print(dict_obj)
df = pd.DataFrame.from_dict(dict_obj, orient ='index') 
df.to_excel("output.xlsx")

