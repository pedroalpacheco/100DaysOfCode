lista = [int(x) for x in input("").split()]
ordenado = "%i\n%i\n%i" %(lista[0], lista[1], lista[2])
lista.sort()

print("%i\n%i\n%i\n\n%s" %(lista[0], lista[1], lista[2], ordenado))




