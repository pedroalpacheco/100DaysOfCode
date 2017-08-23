import unittest
'''
Calcula o MMC de um número inteiro

-Fazer testes da função;
-Fazer validação da entrada de dados;

'''

def mmc():
    try:
        n = int(input("Digite um numero (>1): "))

        fator = 2  # primeiro fator
        while n != 1:
            # conta a multiplicidade de fator em n
            mult = 0;
            while n % fator == 0:
                n = n / fator;
                mult = mult + 1;

            # imprime a multiplicade do fator
            if mult != 0:
                print("fator %d multiplicidade %d" % (fator, mult))

            fator = fator + 1

    except Exception:
        print('Verifique se está digitando números INTEIROS!')

mmc()

"""
class Testmmc(unittest.TestCase):
    def test_mmc(self):
        resultados = (['fator 5 multiplicidade 1','fator 7 multiplicidade 1',
                     'fator 13 multiplicidade 1',
                     'fator 29 multiplicidade 1'])
        self.assertEqual(mmc(13195), resultados)

if __name__ == '__main__':
    unittest.main()
"""