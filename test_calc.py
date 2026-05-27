#Arquivo - contendo os testes unitários para cada módulo da calculadora
import unittest
import calc_potencia
import calc_percentual
import calc_estatistica
import calc_conversao


class TestCalcPotencia(unittest.TestCase):

    def test_potencia(self):
        self.assertEqual(calc_potencia.potencia(5, 2), 25)
        self.assertEqual(calc_potencia.potencia(0, 5), 0)
        self.assertEqual(calc_potencia.potencia(5, 0), 1)
        self.assertEqual(calc_potencia.potencia(-2, 3), -8)

    def test_raiz_quadrada(self):
        self.assertEqual(calc_potencia.raiz_quadrada(36), 6)
        self.assertEqual(calc_potencia.raiz_quadrada(0), 0)
        with self.assertRaises(ValueError):
            calc_potencia.raiz_quadrada(-4)

    def test_raiz_cubica(self):
        self.assertEqual(calc_potencia.raiz_cubica(27), 3)
        self.assertEqual(calc_potencia.raiz_cubica(0), 0)
        self.assertEqual(calc_potencia.raiz_cubica(-27), -3)
        
 class TestCalcPercentual(unittest.TestCase):
	def test_percentual(self):
		self.assertEqual(calc_percentual.percentual(200, 10), 20)

	def test_acrescimo(self):
		self.assertEqual(calc_percentual.acrescimo(200, 10), 220)

	def test_desconto(self):
		self.assertEqual(calc_percentual.desconto(200, 10), 180)

	def test_percentual_zero_porcentagem(self):
		self.assertEqual(calc_percentual.percentual(100, 0), 0.0)

	def test_percentual_zero_valor(self):
		self.assertEqual(calc_percentual.percentual(0, 50), 0.0)

	def test_percentual_negative_porcentagem(self):
		self.assertEqual(calc_percentual.percentual(100, -10), -10.0)

	def test_percentual_negative_valor(self):
		self.assertEqual(calc_percentual.percentual(-100, 10), -10.0)

	def test_percentual_over_100(self):
		self.assertEqual(calc_percentual.percentual(50, 150), 75.0)

	def test_percentual_decimal(self):
		self.assertAlmostEqual(calc_percentual.percentual(99.99, 12.5), 12.49875, places=7)

	def test_invalid_type_none(self):
		with self.assertRaises(TypeError):
			calc_percentual.percentual(None, 10)

	def test_invalid_type_string(self):
		with self.assertRaises(TypeError):
			calc_percentual.acrescimo("100", 10)

	def test_nan_porcentagem(self):
		with self.assertRaises(ValueError):
			calc_percentual.percentual(100, float('nan'))

	def test_inf_valor(self):
		with self.assertRaises(ValueError):
			calc_percentual.desconto(float('inf'), 10)
        
        
class TestCalcEstatistica(unittest.TestCase):

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
        
# kg_para_libras
    def test_kg_valor_normal(self):
        self.assertAlmostEqual(calc_conversao.kg_para_libras(1), 2.20462, places=5)

    def test_kg_zero(self):
        self.assertEqual(calc_conversao.kg_para_libras(0), 0)

    def test_kg_none(self):
        with self.assertRaises(ValueError):
            calc_conversao.kg_para_libras(None)

    def test_kg_tipo_invalido(self):
        with self.assertRaises(TypeError):
            calc_conversao.kg_para_libras("dez")

    def test_kg_negativo(self):
        with self.assertRaises(ValueError):
            calc_conversao.kg_para_libras(-5)

    def test_kg_nan(self):
        with self.assertRaises(ValueError):
            calc_conversao.kg_para_libras(float('nan'))

    def test_kg_infinito(self):
        with self.assertRaises(ValueError):
            calc_conversao.kg_para_libras(float('inf'))
        
unittest.main()

