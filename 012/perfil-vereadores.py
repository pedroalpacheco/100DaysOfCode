import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.camarablu.sc.gov.br/conheca-a-camara/vereadores/')

contsite = (r.text)

#salva requests
with open('vereadores.html', 'w')as f:
    f.write(contsite)

#Le arquivo baixado
with open('vereadores.html', 'r') as b:
    soup = BeautifulSoup(b, 'lxml')

#Apenas para analise
#with open('vereadores_formatado.html', 'w') as c:
#    c.write(soup.prettify())
#salva lista com detalhes de vereadores

soupstr = str(soup.find_all('p'))

with open('detalhesvereadoresblu.txt', 'w') as detalhes:
    detalhes.write(soupstr)


print(soup.find_all('p'))

