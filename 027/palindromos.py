numero = input('Digite um numero:')

lista = list(numero)
listaReverse = [lista[i - 1] for i in range(len(lista), 0, -1)]

if lista == listaReverse:
    print('É um palindromo')
else:
    print('Não é')

#999*989