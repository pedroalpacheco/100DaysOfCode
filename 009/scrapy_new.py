import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.bcb.gov.br/pt-br/#!/home')

resultado = BeautifulSoup(r.text, 'lxml')

#taglist = resultado.find_all('strong')
#taglist = resultado.find_all('strong')

print(resultado.prettify())
