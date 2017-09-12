"""
(ok)-Leia dois valores de pontos flutuantes de dupla precisão A e B, correspondentes a duas notas de alunos.
(ok)-Depois disso, calcule a média do aluno, considerando que o grau A tem peso 3,5 e B tem peso 7,5.
(OK)-Cada nota pode ser de zero a dez, sempre com um dígito após o ponto decimal.
(ok)-Não esqueça de imprimir o fim da linha após o resultado, caso contrário você receberá "Erro de apresentação" .
(ok)-Não esqueça o espaço antes e depois do sinal de igualdade.

Entrada

O arquivo de entrada contém 2 valores de pontos flutuantes com um dígito após o ponto decimal.

Saída

Imprimir MEDIA (média em português) de acordo com o exemplo a seguir, com 5 dígitos após o ponto decimal e com espaço em branco antes e depois do sinal igual.
"""

A = float(input())
B = float(input())

pesoA = A * 3.5
pesoB = B * 7.5

media = pesoA + pesoB
somamedias = 3.5 + 7.5
print('MEDIA = {:.5f}'.format(media/somamedias))