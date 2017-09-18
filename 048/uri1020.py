idade = int(input())

ano = idade // 365
idade %= 365
mes = idade // 30
idade %= 30
dia = idade


print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))


