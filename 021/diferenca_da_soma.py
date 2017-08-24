'''
https://projecteuler.net/problem=6
- A soma dos quadrados dos cem primeiros números naturais é?
- O quadrado da soma dos cem primeiros números naturais é?
- Daí a diferença entre a soma dos quadrados dos cem primeiros números naturais e o quadrado da soma?


The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

-->>Fazer testes;
-->>Fazer validações;

'''

#A soma dos quadrados dos cem primeiros números naturais é?

#Eleva a potencia a lista
#Colocar sempre um valor a mais, exemplo se quise até 10 colocar o valor 11
somaquadrados = [x**2 for x in range(1,101)]
#print (lista)

#soma os resultados elevados a potencia
resultadosomaquadrados = (sum(somaquadrados))
print('>>A soma dos quadrados dos cem primeiros números naturais é : {}'.format(resultadosomaquadrados))

#================================================================

#O quadrado da soma dos cem primeiros números naturais é:

quadradosoma = sum(range(1,101))


resultadoquadradosoma = quadradosoma ** 2

print('>>O quadrado da soma dos cem primeiros números naturais é: {}'.format(resultadoquadradosoma))


#Daí a diferença entre a soma dos quadrados dos cem primeiros números naturais e o quadrado da soma

resultadodiferencas = resultadoquadradosoma - resultadosomaquadrados

print('==>Daí a diferença entre a soma dos quadrados dos cem primeiros números naturais e o quadrado da soma {}'.format(resultadodiferencas))