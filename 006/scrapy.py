import requests
from bs4 import BeautifulSoup

#Extrai texto de site

site=input('Digite o site:')

r = requests.get(site)
soup = BeautifulSoup(r.text, 'lxml')
print(soup.get_text())