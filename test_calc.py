#Arquivo - contendo os testes unitários para cada módulo da calculadora
#Arquivo - contendo os testes unitários para cada módulo da calculadora
import unittest
import calc_conversao

class TestCalcConversao(unittest.TestCase):

    # celsius_para_fahrenheit
    def test_celsius_ponto_de_gelo(self):
        self.assertEqual(calc_conversao.celsius_para_fahrenheit(0), 32)

    def test_celsius_ebulicao(self):
        self.assertEqual(calc_conversao.celsius_para_fahrenheit(100), 212)

    def test_celsius_cruzamento(self):
        self.assertEqual(calc_conversao.celsius_para_fahrenheit(-40), -40)

    def test_celsius_zero_absoluto(self):
        self.assertAlmostEqual(calc_conversao.celsius_para_fahrenheit(-273.15), -459.67, places=2)

    def test_celsius_none(self):
        with self.assertRaises(ValueError):
            calc_conversao.celsius_para_fahrenheit(None)

    def test_celsius_tipo_invalido(self):
        with self.assertRaises(TypeError):
            calc_conversao.celsius_para_fahrenheit("quente")

    def test_celsius_abaixo_zero_absoluto(self):
        with self.assertRaises(ValueError):
            calc_conversao.celsius_para_fahrenheit(-274)

    def test_celsius_nan(self):
        with self.assertRaises(ValueError):
            calc_conversao.celsius_para_fahrenheit(float('nan'))

    def test_celsius_infinito(self):
        with self.assertRaises(ValueError):
            calc_conversao.celsius_para_fahrenheit(float('inf'))

 # km_para_milhas
    def test_km_valor_normal(self):
        self.assertAlmostEqual(calc_conversao.km_para_milhas(1), 0.621371, places=5)

    def test_km_zero(self):
        self.assertEqual(calc_conversao.km_para_milhas(0), 0)

    def test_km_none(self):
        with self.assertRaises(ValueError):
            calc_conversao.km_para_milhas(None)

    def test_km_tipo_invalido(self):
        with self.assertRaises(TypeError):
            calc_conversao.km_para_milhas("dez")

    def test_km_negativo(self):
        with self.assertRaises(ValueError):
            calc_conversao.km_para_milhas(-5)

    def test_km_nan(self):
        with self.assertRaises(ValueError):
            calc_conversao.km_para_milhas(float('nan'))

    def test_km_infinito(self):
        with self.assertRaises(ValueError):
            calc_conversao.km_para_milhas(float('inf'))

unittest.main()