'''

- A soma dos quadrados dos cem primeiros números naturais é?
- O quadrado da soma dos cem primeiros números naturais é?
- Daí a diferença entre a soma dos quadrados dos cem primeiros números naturais e o quadrado da soma?

'''

#A soma dos quadrados dos cem primeiros números naturais é?

#Eleva a potencia a lista
lista = [x**2 for x in range(1,100)]

#soma os resultados elevados a potencia
resultado = (sum(lista))
print('A soma dos quadrados dos cem primeiros números naturais é : {}'.format(resultado))
#================================================================