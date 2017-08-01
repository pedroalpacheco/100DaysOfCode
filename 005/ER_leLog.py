import re


#Funcionou, pegou todos os ids
arquivo = open('log.log', 'r')
le_arquivo = arquivo.read()
#print(le_arquivo)
resultado = re.findall(r'\*+ \w+ (\d+.\d+)', le_arquivo)
print(resultado)