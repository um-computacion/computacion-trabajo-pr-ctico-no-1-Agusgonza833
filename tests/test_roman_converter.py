import unittest
from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):
    def test_basic_numbers(self):
        """Prueba números básicos"""
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")
        self.assertEqual(decimal_to_roman(50), "L")
        self.assertEqual(decimal_to_roman(100), "C")
        self.assertEqual(decimal_to_roman(500), "D")
        self.assertEqual(decimal_to_roman(1000), "M")
    
    def test_simple_combinations(self):
        """Prueba combinaciones simples de símbolos"""
        self.assertEqual(decimal_to_roman(2), "II")
        self.assertEqual(decimal_to_roman(3), "III")
        self.assertEqual(decimal_to_roman(6), "VI")
        self.assertEqual(decimal_to_roman(7), "VII")
        self.assertEqual(decimal_to_roman(8), "VIII")
        self.assertEqual(decimal_to_roman(11), "XI")
        self.assertEqual(decimal_to_roman(15), "XV")
        self.assertEqual(decimal_to_roman(16), "XVI")
        self.assertEqual(decimal_to_roman(30), "XXX")
    
    def test_subtraction_rules(self):
        """Prueba reglas de sustracción"""
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")
        self.assertEqual(decimal_to_roman(400), "CD")
        self.assertEqual(decimal_to_roman(900), "CM")
    
    def test_complex_numbers(self):
        """Prueba números complejos"""
        self.assertEqual(decimal_to_roman(14), "XIV")
        self.assertEqual(decimal_to_roman(19), "XIX")
        self.assertEqual(decimal_to_roman(24), "XXIV")
        self.assertEqual(decimal_to_roman(49), "XLIX")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(499), "CDXCIX")
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
        self.assertEqual(decimal_to_roman(1984), "MCMLXXXIV")
        self.assertEqual(decimal_to_roman(2023), "MMXXIII")
        self.assertEqual(decimal_to_roman(3549), "MMMDXLIX")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")
    
    def test_boundary_values(self):
        """Prueba valores límite"""
        self.assertEqual(decimal_to_roman(1), "I")  # Valor mínimo
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")  # Valor máximo
        
        # Valores fuera de rango deben lanzar una excepción
        with self.assertRaises(ValueError):
            decimal_to_roman(0)
        
        with self.assertRaises(ValueError):
            decimal_to_roman(4000)
        
        with self.assertRaises(ValueError):
            decimal_to_roman(-1)

if _name_ == "_main_":
    unittest.main()
   