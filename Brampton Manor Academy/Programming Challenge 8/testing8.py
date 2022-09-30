import unittest
import throbac


class TestingThrobac(unittest.TestCase):

    def test_conversions(self):
        self.assertEqual(throbac.rome_to_int('XLIV'), 44)
        self.assertEqual(throbac.int_to_rome(309), 'CCCIX')


if __name__ == '__main__':
    unittest.main()
