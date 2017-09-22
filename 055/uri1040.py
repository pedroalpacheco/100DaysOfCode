notas = input().split(' ')
Num, Ndois, Ntres, Nquatro = notas

#Média
notapesoUM = float(Num) * 2 / 10
notapesoDOIS = float(Ndois) * 3 / 10
notapesoTRES = float(Ntres) * 4 / 10
notapesoQUATRO = float(Nquatro) * 4 / 10
MEDIA = notapesoUM + notapesoDOIS + notapesoTRES + notapesoQUATRO / 4

#print(MEDIA)

if MEDIA >= 7.0:
    print('Media: {:.1f}'.format(MEDIA))
    print('Aluno aprovado.')
elif MEDIA < 5.0:
    print('Media: {:.1f}'.format(MEDIA))
    print('Aluno reprovado.')
elif MEDIA > 5 and MEDIA < 6.9:
    print('Aluno em exame.')
    notaEXAME = float(input('Nota do exame: '))
    totExame = notaEXAME + MEDIA / 2
    if totExame < 4.9:
        print('Aluno reprovado')
        print('Media final: {:.1f}'.format(totExame))
    else:
        print('Aluno aprovado')
        print('Media final: {:.1f}'.format(totExame))
        print('Media:{:.1f}'.format(MEDIA))
        print('Media exame:{:.1f}'.format(totExame))
