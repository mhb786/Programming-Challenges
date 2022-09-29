import unittest
import rods


class TestRods(unittest.TestCase):

    def test_meters(self):
        self.assertEqual(rods.meters(10), 50.292)
        self.assertEqual(rods.feet(50.292), 165.0)


if __name__ == '__main__':
    unittest.main()
