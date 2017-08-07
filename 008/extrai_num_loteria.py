from bs4 import BeautifulSoup
import re

with open('D_MEGA.HTM', encoding='latin-1') as f:
    soup = BeautifulSoup(f, 'lxml')


formhtml = soup.prettify()
expressao = re.findall(r'\d{2}', formhtml)

print(expressao)
