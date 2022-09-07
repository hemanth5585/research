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