import unittest
import latinsquare

class TestLatinSquare(unittest.TestCase):

    def test_square(self):
        self.assertEqual(latinsquare.latinsquare(1, 0, 0), 4)

if __name__ == '__main__':
    unittest.main()
