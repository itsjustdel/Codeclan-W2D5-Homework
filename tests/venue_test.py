import unittest
from classes.venue import Venue

class TestVenue(unittest.TestCase):

    def test_venue_entryFee_is_10(self):
        # Arrange
        venue = Venue(10)
        # Act
        actual = venue.entry_fee
        expected = 10
        # Assert
        self.assertEqual(actual, expected)
