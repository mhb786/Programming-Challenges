import unittest
import isbn


class TestISBN(unittest.TestCase):

    def test_meters(self):
        self.assertEqual(isbn.find_missing_digit('15688?111X'), 5)
        self.assertEqual(isbn.find_missing_digit('812071988?'), 3)
        self.assertEqual(isbn.find_missing_digit('020161586?'), 'X')
        self.assertEqual(isbn.find_missing_digit('?131103628'), 0)
        self.assertEqual(isbn.find_missing_digit('?86046324X'), 'X')
        self.assertEqual(isbn.find_missing_digit('1?68811306'), 1)
        self.assertEqual(isbn.find_missing_digit('951?451570'), 4)
        self.assertEqual(isbn.find_missing_digit('0393020?31'), 2)
        self.assertEqual(isbn.find_missing_digit('01367440?5'), 9)


if __name__ == '__main__':
    unittest.main()