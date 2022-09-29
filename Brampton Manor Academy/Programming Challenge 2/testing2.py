import unittest
import richter

class TestRichter(unittest.TestCase):

    def test_joules(self):
        self.assertEqual(richter.joules(3.4), 7943282347.242789)

    def test_tnt(self):
        self.assertEqual(richter.tnt(7943282347.242789), 1.8984900447521007)


if __name__ == '__main__':
    unittest.main()
