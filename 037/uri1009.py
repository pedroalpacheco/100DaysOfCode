vendedor = 'MANGOJATA'
#vendedor = input()
salariofixo = 1700.00
#salariofixo = float(input())
vendas = 1230.50
#vendas = float(input())

comicao = 15 * vendas /100

total = salariofixo + comicao

print('TOTAL = R$ {:.2f}'.format(total))