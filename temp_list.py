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

base_url = "https://en.wikipedia.org"

head = []
link = []
check = []
topics = []
excel = openpyxl.Workbook() 
sheet = excel.active    
sheet.title = "Chapters"
path_of_excel = "C:/Users/chhem/OneDrive/Desktop/Project/Dataset/Dataset.xlsx"
path_of_excel1 = "C:/Users/chhem/OneDrive/Desktop/Project/Dataset/output.xlsx"
def function():
    i = 1
    while i < len(head):
        print(i)
        print(head[i])
        print(link[i])
        print(check[i])
        if check[i]==False:
            check[i] =True
            df = pd.DataFrame(pd.read_excel(path_of_excel))
            url = link[i]
            topics.clear()
            source = requests.get(url)
            source.raise_for_status()
            soup = BeautifulSoup(source.text,'html.parser')  
            try:  
                if soup.find("span",class_="mw-page-title-main"):
                    heading = soup.find("span",class_="mw-page-title-main")
                heading = heading.text
                summary = wiki.summary(heading)
                topics.append(heading)
                topics.append(summary)
            except:
                print("Somthing went wrong so no data")
            for tag in soup.select('p a[title]'):      
                topic = tag['title']
                topics.append(topic)
            excel = openpyxl.Workbook()
            sheet = excel.active    
            sheet.title = "Chapters"
            df2 = pd.DataFrame([topics])
            df = pd.concat([df,df2],ignore_index=True)
            df.to_excel("Dataset.xlsx")
            #print(head)
            op = pd.DataFrame(pd.read_excel(path_of_excel1))
            head_temp= []
            for tag in soup.select('p a'):
                topic = tag['href']
                if topic.startswith('#') or topic.startswith('http'):
                    a = 0
                else:
                    reduced_string = re.sub(r'.', '', topic, count = 6)
                    result = reduced_string.replace('_', ' ')
                    topic = base_url + topic
                    #result  = topic name
                    #topic   = url
                    if result in head:
                        continue
                    check.append(False)
                    head_temp.append(result)
                    head.append(result)
                    link.append(topic)
            #print(head)

            df1 = pd.DataFrame(list(zip(head_temp,link)))
            op = pd.concat([op,df1],ignore_index=True)
            op.to_excel("output.xlsx")
            head_temp.clear()
            #print(op)
        if i == 150:
            break
        i=i+1
    return


first_url ="/wiki/React_(JavaScript_library)"
url = base_url+first_url
print(url)
source = requests.get(url)
source.raise_for_status()
soup = BeautifulSoup(source.text,'html.parser')    
if soup.find("span",class_="mw-page-title-main"):
    heading = soup.find("span",class_="mw-page-title-main")
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
new_df = pd.DataFrame([topics])
#print(new_df)
new_df.to_excel("Dataset.xlsx")



i = 0 
title = ""
for tag in soup.select('p a'):
    topic = tag['href']
    
    if topic.startswith('#') or topic.startswith('http'):
        a = 0
    else:
        reduced_string = re.sub(r'.', '', topic, count = 6)
        result = reduced_string.replace('_', ' ')
        topic = base_url + topic
        #result  = topic name
        #topic   = url
        check.append(False)
        head.append(result)
        link.append(topic)
df = pd.DataFrame(list(zip(head,link)))
df.to_excel("output.xlsx")

function()