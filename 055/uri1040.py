notas = input().split(' ')
Num, Ndois, Ntres, Nquatro = notas

MEDIA = ((float(Num)*2)+(float(Ndois)*3)+(float(Ntres)*4)+float(Nquatro))/10


if MEDIA >= 7.0:
    print('Media: {:.1f}'.format(MEDIA))
    print('Aluno aprovado.')
elif MEDIA < 5.0:
    print('Media: {:.1f}'.format(MEDIA))
    print('Aluno reprovado.')

elif MEDIA > 5.0 and MEDIA < 6.9:
    print('Media: {:.1f}'.format(MEDIA))
    print('Aluno em exame.')

    notaEXAME = float(input( ))
    totExame = (notaEXAME + MEDIA) / 2
    if totExame < 4.9:
        print('Aluno reprovado')
        print('Media final: {:.1f}'.format(totExame))
    else:
        print('Aluno aprovado')
        print('Media final: {:.1f}'.format(totExame))


