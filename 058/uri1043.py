

a, b, c = (float(x) for x in input("").split())

verificaum = (b-c) < a < (b+c)
verificadois = (a-c) < b < (a+c)
verificatres = (a-b) < c < (a+b)

if verificaum == True and verificadois == True and verificatres == True:
    perimetro = a + b + c
    print('Perimetro = {}'.format(perimetro))
else:
    minimo = min(a, b, c)
    if a == minimo:
        area = ((b+c)*a)/2
        print('Area = {:.1f}'.format(area))
    elif b == minimo:
        area = ((a+c)*b)/2
        print('Area = {:.1f}'.format(area))
    else:
        area = ((a+b)*c)/2
        print('Area = {:.1f}'.format(area))
