import unittest
from app import calcula


class TestFatorial(unittest.TestCase):

    def test_fatorial(self):
        self.assertEqual(calcula(1,1), 2)

if __name__ == '__main__':
    unittest.main()