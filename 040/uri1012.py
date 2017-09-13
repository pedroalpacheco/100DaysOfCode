leitura = input().split(' ')

A,B,C = leitura

areatriangulo = (float(A)*float(C))/2
circulo = float(C)**2*3.14159
trapezio = (float(A)+float(B))/2*float(C)
quadrado = float(B) * float(B)
retangulo = float(A) * float(B)

print('TRIANGULO: {:.3f}'.format(areatriangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))