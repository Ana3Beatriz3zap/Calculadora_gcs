import unittest
import calc_potencia

# O segredo está em criar uma classe que herda de unittest.TestCase
class TestCalculadora(unittest.TestCase):

    def test_potencia(self):
        self.assertEqual(calc_potencia.potencia(5, 2), 25)

    def test_raiz_quadrada(self):
        self.assertEqual(calc_potencia.raiz_quadrada(36), 6)

    def test_raiz_cubica(self):
        self.assertEqual(calc_potencia.raiz_cubica(27), 3)

if __name__ == '__main__':
    unittest.main()