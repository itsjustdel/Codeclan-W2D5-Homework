import unittest
from classes.bar import Bar

class TestBar(unittest.TestCase):
    
    def setUp(self):
        self.bar = Bar()

    def test_bar__get_Pina_Colada_price(self):        
        # Act
        actual = self.bar.drinks["Pina Colada"]
        expected = 6.95
        # Assert
        self.assertEqual(actual, expected)

    def test_bar__total_drinks_available_is_3(self):
        # Act
        actual = len(self.bar.drinks)
        expected = 3
        # Assert
        self.assertEqual(actual, expected)
