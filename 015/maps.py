import webbrowser
import sys
import pyperclip

'''
Como usar:
python maps.py numero da rua ',' endereço ',' cidade
'''

sys.argv

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com.br/maps/place/' + address)