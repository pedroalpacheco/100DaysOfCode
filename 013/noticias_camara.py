import requests
from bs4 import BeautifulSoup

url = 'http://www.camarablu.sc.gov.br/comunicacao/releases/?future=false'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

div = soup.find('div', {'id':'content'})
print(div)

with open('not.html', 'w', encoding='utf-8') as f:
    f.write(r.text)
