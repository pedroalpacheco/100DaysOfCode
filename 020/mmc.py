import unittest
'''
Calcula o MMC de um número inteiro

'''

def mmc(n):
    try:

        fator = 2
        while n != 1:

            mult = 0;
            while n % fator == 0:
                n = n / fator;
                mult = mult + 1;


            if mult != 0:
                return fator
                #print(fator)


            fator = fator + 1

    except Exception:
        print('Verifique se está digitando números INTEIROS!')

mmc()


class Testmmc(unittest.TestCase):
    def test_mmc(self):
        self.assertEqual(mmc(4), 2)

if __name__ == '__main__':
    unittest.main()
