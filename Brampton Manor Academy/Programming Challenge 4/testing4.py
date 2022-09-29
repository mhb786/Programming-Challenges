import unittest
import windchill

class TestWindchill(unittest.TestCase):

    def test_calculation(self):
        self.assertEqual(windchill.calculation(3.5, 18), -16.47884113003356)
        self.assertEqual(windchill.calculation(10,14), -6.05660500717706)
        self.assertEqual(windchill.calculation(0,25), -24.093780999553864)
        self.assertEqual(windchill.calculation(-10, 35), -41.16894662953316)

if __name__ == '__main__':
    unittest.main()
