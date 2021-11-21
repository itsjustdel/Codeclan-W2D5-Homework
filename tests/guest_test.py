import unittest
from classes.guest import Guest
from classes.venue import Venue
from classes.room import Room
from classes.song import Song
from classes.bar import Bar


class TestGuest(unittest.TestCase):

    def setUp(self):
        # make a guest, we will use this guest multiple times
        # so let's make it in setUp
        self.guest = Guest("Del", "Like Herod", 100)
        # create a venue instance to hold entry fee
        self.venue = Venue(10,6,100.00)
        # make a 
        self.room = Room(0,6)

    def test_guest__name_is_Del(self):
        expected = "Del"
        actual = self.guest.name
        self.assertEqual(actual, expected)

    def test_guest__fav_song_is_Like_Herod(self):
        # Act
        expected = "Like Herod"
        actual = self.guest.fav_song
        # Assert
        self.assertEqual(actual, expected)    
    
    def test_guest__money_was_reduced(self):
        # Arrange
        self.guest.reduce_money(self.venue.entry_fee)
        # Act 
        expected = 90
        actual = self.guest.money
        # Assert 
        self.assertEqual(actual,expected)

    def test_guest__can_pay_in_false(self):
        # Act
        expected = True
        actual = self.guest.pay_in(self.venue.entry_fee)
        # Assert
        self.assertEqual(actual, expected)

    def test_guest__can_pay_in_true(self):
        # Act
        expected = True
        actual = self.guest.pay_in(self.venue.entry_fee)
        # Assert
        self.assertEqual(actual, expected)

    def test_guest__room_has_fav_song_woohoo(self):
        # Arrange
        song = Song("Like Herod", "Mogwai", 6.5)
        self.room.add_song_to_room(song)

        # Act        
        expected = "Woohoo!"
        actual = self.guest.room_has_fav_song(self.room, song)
        self.assertEqual(actual, expected)

    def test_guest__add_drink_to_tab(self):
        # Arrange
        # make a new bar for this test
        bar = Bar()        
        # Act
        bar.add_drink_to_tab("Pina Colada", self.room)

        expected = 1
        actual = len ( self.room.bar_tab)

        # Assert
        self.assertEqual(actual, expected)

        
    

    