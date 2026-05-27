#Arquivo - contendo os testes unitários para cada módulo da calculadoraimport unittest
import calc_estatistica

class TestEstatistica(unittest.TestCase):

    def test_media(self):
        self.assertEqual(
            calc_estatistica.media([2, 4, 6, 8]), 5
        )

    def test_mediana(self):
        self.assertEqual(
            calc_estatistica.mediana([1, 3, 5]), 3
        )

    def test_moda(self):
        self.assertEqual(
            calc_estatistica.moda([1, 2, 2, 3]), 2
        )

if __name__ == '__main__':
    unittest.main()