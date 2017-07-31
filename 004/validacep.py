#Valida Cep
import unittest
import re

def cep(digcep):
    regexcep = re.compile('\d{5}\-\d{3}')
    resultcep = regexcep.match(digcep) is None
    if resultcep == True:
        resultado = "CEP invalido!"
    else:
        resultado = "CEP valido"

    return resultado
    #print(resultado)


cep('89022-390')


#Realiza teste
class TestCep(unittest.TestCase):

    def test_cep(self):
        self.assertEqual(cep('89012-500'), 'CEP valido')#False se reconhece como cep

if __name__ == '__main__':
    unittest.main()