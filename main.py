from bs4 import BeautifulSoup
import requests

url = 'https://durham.cioc.ca/volunteer/results.asp?CMID=65%2C68%2C72%2C74%2C80%2C2283&Age=16&forOSSD=on&IGID=1%2C+2%2C+5%2C+7%2C+25%2C+8%2C+10%2C+14%2C+15%2C+17%2C+18%2C+19%2C+20%2C+21%2C+24'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

divs = soup.find_all('div', class_='vol-results-position-title')
with open("opportunities.txt", 'w') as f:
    for div in divs:
        print(div.a.string)
        f.write(div.a.string + '\n')