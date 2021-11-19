import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Like Herod", "Mogwai", 6.5)

    def test_song__return_Like_Herod(self):        
        expected = "Like Herod"
        actual = self.song.name
        self.assertEqual(actual, expected)

    def test_song__return_Mogwai(self):
        expected = "Mogwai"
        actual = self.song.artist
        self.assertEqual(actual, expected)

    def test_song__return_6_point_5(self):
        expected = 6.5
        actual = self.song.length
        self.assertEqual(actual, expected)
