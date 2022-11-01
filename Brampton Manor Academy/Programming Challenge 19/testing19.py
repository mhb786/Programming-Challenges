import unittest
import modern_art


class TestArt(unittest.TestCase):

    def test_meters(self):
        self.assertEqual(modern_art.arrangement([1, 2, 1, 0], 8), 'BCAB')
        self.assertEqual(modern_art.arrangement([2, 2, 2, 2], 2520), 'DDCCBBAA')
        self.assertEqual(modern_art.arrangement([0, 3, 0, 3], 1234567), 'DBBDBD')


if __name__ == '__main__':
    unittest.main()