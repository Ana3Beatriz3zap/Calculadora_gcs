"""Arquivo contendo os testes unitários da calculadora."""

import unittest

import calc_percentual


class TestCalcPercentual(unittest.TestCase):
	def test_percentual(self):
		self.assertEqual(calc_percentual.percentual(200, 10), 20)

	def test_acrescimo(self):
		self.assertEqual(calc_percentual.acrescimo(200, 10), 220)

	def test_desconto(self):
		self.assertEqual(calc_percentual.desconto(200, 10), 180)


if __name__ == "__main__":
	unittest.main()