
def triangulo():
    medidas = input()
    numeros = [float(s) for s in medidas.split()]
    numeros.sort(reverse=True)
    A, B, C = numeros

    if A >= B + C:
        print("NAO FORMA TRIANGULO")
    else:
        if A*A == B*B + C*C:
            print("TRIANGULO RETANGULO")
        if A*A > B*B + C*C:
            print("TRIANGULO OBTUSANGULO")
        if A*A < B*B + C*C:
            print("TRIANGULO ACUTANGULO")
        if A == B and B == C:
            print("TRIANGULO EQUILATERO")
        elif A == B or A == C or B == C:
            print("TRIANGULO ISOSCELES")

if __name__ == '__main__':
    triangulo()

