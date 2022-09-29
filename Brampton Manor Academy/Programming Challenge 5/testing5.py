import unittest
import slayer

class TestSlayer(unittest.TestCase):

    def test_slayer(self):
        self.assertEqual(slayer.answer(142857), 428571)
        self.assertEqual(slayer.layers(142857), 428571)


if __name__ == '__main__':
    unittest.main()
