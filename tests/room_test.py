import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(0,6)
        self.guest = Guest("Del", "Like Herod", 100)

    def test_room__room_number_is_0(self):
        # Act
        actual = self.room.number
        expected = 0
        # Assert
        self.assertEqual(actual, expected)

    def test_room__max_guests_is_6(self):
        # Act
        actual = self.room.max_guests
        expected = 6
        # Assert
        self.assertEqual(actual, expected)
    
    def test_room__guests_length_is_1_after_adding(self):       
        # Act
        self.room.check_in_guest(self.guest)
        actual = len (self.room.guests )
        expected = 1
        # Assert
        self.assertEqual(actual, expected)

    def test_room__guests_length_is_0_after_removing(self):
        # Act
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        actual = len (self.room.guests )
        expected = 0
        # Assert
        self.assertEqual(actual, expected)

    def test_room__song_added(self):
        # Arrange
        song = Song("2 Rights Make 1 Wrong", "Mogwai", 8.23)
        # Act
        self.room.add_song_to_room(song)
        actual = len(self.room.songs)
        expected = 1
        # Assert        
        self.assertEqual(actual, expected)

    def test_room__is_room_full_true(self):
        # Arrange
        # populate room
        for i in range(0, 20):
            self.room.check_in_guest(Guest(str(i), "Like Herod", i))

        # Act
        actual = self.room.is_room_full()
        expected = True

        # Assert
        self.assertEqual(actual, expected)

    def test_room__is_room_full_false(self):
        # Arrange
        # populate room, but not too much!    
        self.room.check_in_guest(Guest("Billy", "Like Herod", 10))

        # Act
        actual = self.room.is_room_full()
        expected = False

        # Assert
        self.assertEqual(actual, expected)

    def test_room__has_song_true(self):
        # Arrange
        # add the song we want to check for 
        song = Song("Take Me Somewhere Nice", "Mogwai", 8.23)
        self.room.add_song_to_room(song)
        
        # Act
        actual = self.room.has_song(song)
        expected = True

        # Assert
        self.assertEqual(actual, expected)

    def test_room__has_song_false(self):
        # Arrange
        # add the song we want to check for
        song = Song("East Hastings", "Godspeed You! Black Emperor", 16.45)
        # Act
        actual = self.room.has_song(song)
        expected = False

        # Assert
        self.assertEqual(actual, expected)