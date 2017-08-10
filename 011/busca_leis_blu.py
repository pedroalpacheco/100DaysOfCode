import requests


def buscandoCamara(busca):
    url = 'http://www.camarablu.sc.gov.br/?s={0}'.format(busca)
    r = requests.get(url)
    cookie = r.cookies.get_dict()
    r = requests.get(url, cookies=cookie)
    with open('busca_camara_{}.html'.format(busca), 'w') as f:
        f.write(r.text)

buscandoCamara('transito')

