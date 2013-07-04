import unittest
from Bissexto import Bissexto

class BissextoTest(unittest.TestCase):	

	def test_is_bissexto_with_4_should_return_true(self):
		bissexto = Bissexto()
		result = bissexto.is_bissexto(4)
		self.assertTrue(result)

	def test_is_bissexto_with_8_should_return_true(self):
		bissexto = Bissexto()
		result = bissexto.is_bissexto(8)
		self.assertTrue(result)
	
	def test_is_bissexto_with_200_should_return_false(self):
		bissexto = Bissexto()
		result = bissexto.is_bissexto(200)
		self.assertFalse(result)

	def test_is_bissexto_with_400_should_return_true(self):
		bissexto = Bissexto()
		result = bissexto.is_bissexto(400)
		self.assertTrue(result)

unittest.main()

		
