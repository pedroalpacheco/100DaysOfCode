#Regex valida ip
import re

import unittest
import re




def ip(digip):
    regexip = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    resultip = regexip.match(digip) is None
    if resultip == True:
        resultado = "IP invalido!"
    else:
        resultado = "IP valido"

    return resultado
    #print(resultado)


ip('172.21.3.1')


#Realiza teste
class TestIp(unittest.TestCase):

    def test_ip(self):
        self.assertEqual(ip('192.168.0.1'), 'IP valido')#False se reconhece como ip

if __name__ == '__main__':
    unittest.main()