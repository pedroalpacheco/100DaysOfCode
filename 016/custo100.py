import unittest

'''
Calcula o quanto de tempo você precisa para ganhar R$100,00
'''


def salariohora(salario, horastrab):
    """Calcula hora"""
    vlhora = salario / horastrab
    vlcem = 100 / vlhora
    vlcemformat = ("{0:.2f}".format(round(vlcem, 2)))  # formata número
    return vlcemformat


horascem = salariohora(4128, 160)

print('Para ganha R$ 100 voce deve trabalhar {} horas'.format(horascem))

#------------------------------------------------

class TestCem(unittest.TestCase):
    """Realiza testes"""
    def test_salariohora(self):
        self.assertEqual(salariohora(3000, 160), '5.33')

if __name__ == '__main__':
    unittest.main()
#------------------------------------------------
