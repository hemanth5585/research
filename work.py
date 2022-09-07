
from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = "Chapters"
sheet.append(['sub-topic'])
print(excel)

url = "https://en.wikipedia.org/wiki/React_(JavaScript_library)"
source = requests.get("https://en.wikipedia.org/wiki/React_(JavaScript_library)")
source.raise_for_status()
soup = BeautifulSoup(source.text,'html.parser')
heading = soup.find("span",class_="mw-page-title-main").text
print(heading)  
for tag in soup.select('p a[href]'):
    topic = tag['href']
    sheet.append([topic])
excel.save("DataSet.xlsx")


