
def menu():

    pedidos = input().split(' ')

    a, b = pedidos

    if a == '1':
        valor = float(b) * 4.00
        print('Total: R$ {:.2f}'.format(valor))
    elif a == '2':
        valor = float(b) * 4.50
        print('Total: R$ {:.2f}'.format(valor))
    elif a == '3':
        valor = float(b) * 5.00
        print('Total: R$ {:.2f}'.format(valor))
    elif a == '4':
        valor = float(b) * 2.00
        print('Total: R$ {:.2f}'.format(valor))
    elif a == '5':
        valor = float(b) * 1.50
        print('Total: R$ {:.2f}'.format(valor))
    else:
        print('Codigo não encontrado!')

menu()

"""
pedidos = input().split(' ')

a, b = pedidos

if a == '1':
    valor = float(b) * 4.00
    print('Total: R$ {:.2f}'.format(valor))
elif a == '2':
    valor = float(b) * 4.50
    print('Total: R$ {:.2f}'.format(valor))
elif a == '3':
    valor = float(b) * 5.00
    print('Total: R$ {:.2f}'.format(valor))
elif a == '4':
    valor = float(b) * 2.00
    print('Total: R$ {:.2f}'.format(valor))
elif a == '5':
    valor = float(b) * 1.50
    print('Total: R$ {:.2f}'.format(valor))
else:
    print('Codigo não encontrado!')
"""