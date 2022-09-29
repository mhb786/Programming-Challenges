import unittest
import trick99


class Testing99Trick(unittest.TestCase):

    def test_calculation(self):
        self.assertEqual(trick99.calculation_result(72, 84), 15)


if __name__ == '__main__':
    unittest.main()
