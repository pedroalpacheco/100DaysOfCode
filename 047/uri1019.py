
import unittest

def converte_segundos(segundos):
    segundos = int(input())

    hora = segundos / 3600
    segundos %= 3600
    minutes = segundos / 60
    segundos %= 60
    seconds = segundos
    return "%d:%d:%d" % (hora, minutes, seconds)


# testes ------
class TestConversao(unittest.TestCase):

    def test_segundos(self):
        self.assertTrue(converte_segundos(140153), '38:55:53')


if __name__ == '__main__':
    unittest.main()


