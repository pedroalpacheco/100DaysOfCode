
"""
def notas_total(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    totais = []
    for idx, nota in enumerate(notas):
        totais.append(0)
        if valor > nota:
            totais[idx] = int(valor / nota)
            valor -= totais[idx] * nota
    return notas, totais


numero = int(input())
# numero = 11257
print('Entrada:\n{}\n'.format(numero))
notas, totais = notas_total(numero)
print('Saida:')
masc = '{} nota{} de R$ {},00'
for nota, total in zip(notas, totais):
    if total:
        print(masc.format(total, 's' if total > 1 else '', nota))
"""
value = int(input());
val = value;
cem = cinquenta = vinte = dez = cinco = dois = um = 0;

if int(value/100) >= 1:
    cem = int(value/100);
    value -= cem*100;

if int(value/50) >= 1:
    cinquenta = int(value/50);
    value -= cinquenta*50;

if int(value/20) >= 1:
    vinte = int(value/20);
    value -= vinte*20;

if int(value/10) >= 1:
    dez = int(value/10);
    value -= dez*10;

if int(value/5) >= 1:
    cinco = int(value/5);
    value -= cinco*5;

if int(value/2) >= 1:
    dois = int(value/2);
    value -= dois*2;

if int(value/1) >= 1:
    um = int(value/1);
    value -= um*1;

print("%d" % val);
print("%d nota(s) de R$ 100,00" % cem);
print("%d nota(s) de R$ 50,00" % cinquenta);
print("%d nota(s) de R$ 20,00" % vinte);
print("%d nota(s) de R$ 10,00" % dez);
print("%d nota(s) de R$ 5,00" % cinco);
print("%d nota(s) de R$ 2,00" % dois);
print("%d nota(s) de R$ 1,00" % um);