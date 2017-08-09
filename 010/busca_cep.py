import requests

def buscandoCep(cep):
    """Faz a busca pelo cep no site dos correios cep"""
    url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
    payload = {'relaxation': cep, 'tipoCEP': 'ALL', 'semelhante': 'N'}
    response = requests.post(url, data=payload)
    with open('correios_resultado.html', 'w') as f:
        f.write(response.text)

buscandoCep('xxxxx-xxx')