
leitura = input().split(' ')

a, b, c = leitura

maior = (int(a) + int(b) + abs(int(a) - int(b)))/2

total = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print("%d eh o maior" %total)
