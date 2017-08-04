import requests
from bs4 import BeautifulSoup


def site_texto(site):
    """Salva em texto o site"""
    r = requests.get(site)
    soup = BeautifulSoup(r.text, 'lxml')
    text_site = (soup.get_text())
    arq = open('site.txt', 'w')
    arq.write(text_site)
    arq.close()

osite = input('Digite o site:')
site_texto(osite)