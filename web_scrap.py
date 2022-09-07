from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = "Topics"
sheet.append(['Topic','Link'])
print(excel)

try:
    url = "https://en.wikipedia.org/wiki/React_(JavaScript_library)"
    source = requests.get("https://en.wikipedia.org/wiki/React_(JavaScript_library)")
    source.raise_for_status()
    soup = BeautifulSoup(source.text,'html.parser')
    heading = soup.find('h1',class_="firstHeading").text
    it = soup.find('div',class_="toc").find_all("li")
    all_links = [tag['href'] for tag in soup.select('p a[href]')]
    for i in it:
        topic = i.find('span',class_="toctext").text
        links = i.find('a').get('href')
        links = url+links
        print(links)
        print(topic)
        sheet.append([topic,links])
        break
    print(heading)

except Exception as e:
    print(e)
excel.save("DS.xlsx")

'''
Working Code 

from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = "Chapters"
sheet.append(['opic'])
print(excel)

url = "https://en.wikipedia.org/wiki/React_(JavaScript_library)"
source = requests.get("https://en.wikipedia.org/wiki/React_(JavaScript_library)")
source.raise_for_status()
soup = BeautifulSoup(source.text,'html.parser')
c=0
for tag in soup.select('p a[href]'):
    print(tag['href'])
    c=c+1
print(c)


'''
'''
from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = "Chapters"
sheet.append(['Topic'])
print(excel)

url = "https://en.wikipedia.org/wiki/React_(JavaScript_library)"
source = requests.get("https://en.wikipedia.org/wiki/React_(JavaScript_library)")
source.raise_for_status()
soup = BeautifulSoup(source.text,'html.parser')
all_links = [tag['href'] for tag in soup.select('p a[href]')]
print(all_links)
sheet.append(all_links)
excel.save("format.xlsx")

'''