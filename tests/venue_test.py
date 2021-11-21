import unittest
from classes.venue import Venue

class TestVenue(unittest.TestCase):

    def setUp(self):
        self.venue = Venue(10, 6, 100.00)

    def test_venue_entryFee_is_10(self):        
        # Act
        actual = self.venue.entry_fee
        expected = 10
        # Assert
        self.assertEqual(actual, expected)

    def test_venue__make_new_venue_has_rooms_6(self):        
        # Act 
        actual = len(self.venue.rooms)
        expected = 6
        # Assert
        self.assertEqual(actual, expected)

    def test_venue__bar_has_drinks_true(self):
        #test there are some drinks
        actual = len (self.venue.bar.drinks)
        self.assertGreater(actual, 0)

    
