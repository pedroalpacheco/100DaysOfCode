# -*- coding: utf-8 -*-
#Print de tela de site
#Coleta de informações
from datetime import datetime
from PIL import Image
from PIL import ImageDraw
import subprocess

# Pega data e hora
agora = datetime.now()
hoje = str(agora)

site = input("Digite a url :")
jornal = input("Digite o nome do site :")
jornalista = input("Digite jornalista :")

ext = ".png"

subprocess.check_call(['cutycapt', '--url='+site, '--out='+jornalista+ext])


#Adiciona data
img = Image.open(jornalista+ext)
draw = ImageDraw.Draw(img)
texto = hoje
#pos = 100,100
pos = 10,10
draw.text(pos, texto)
img.save('tex_'+hoje+jornalista+ext)