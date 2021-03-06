import unittest

from Song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Odin", "Manowar", "The Sons of Odin", "3:44")
        self.other_song = Song("Odin", "Manowar", "The Sons of Odin", "3:44")

    def test_init(self):
        self.assertTrue(isinstance(self.song, Song))

    def test_srt(self):
        self.assertEqual(str(self.song),"Manowar - Odin form The Sons of Odin - 3:44")

    def test_eq(self):
        self.assertEqual(self.song,self.other_song)

    def test_hash(self):
        self.assertIsNotNone(hash(self.song))
        self.assertTrue(isinstance(hash(self.song), int))

    def test_length(self):
        pass



if __name__ == '__main__':
    unittest.main()
