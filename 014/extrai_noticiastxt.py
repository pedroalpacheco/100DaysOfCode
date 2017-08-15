import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()

site = 'http://www.camarablu.sc.gov.br/comunicacao/releases/?future=false'


def baixa_site(url):
    """Low infos of site, used requests"""
    r = requests.get(url)
    with open('noticias_brutas.html', 'w') as f:
        f.write(r.text)


def filtra_noticias():
    with open('noticias_brutas.html', 'r') as g:
        soup = BeautifulSoup(g, 'lxml')
        noticias = soup.find_all(['p'])
        noticiasstr = str(noticias)
        relatNoticias = 'noticias-{0}.txt'.format(now)
        with open(relatNoticias, 'w') as h:
            h.write(noticiasstr)

baixa_site(site)
filtra_noticias()