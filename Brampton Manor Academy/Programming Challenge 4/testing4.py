from windchill import calculation

class MyFirstTests(calculation.TestCase):

    def test_calculation(self):
        self.assertEqual(calculation(10,14), -6.5895344209562525)
        self.assertEqual(calculation(0,25), -24.093780999553864)
        self.assertEqual(calculation(-10, 35), -41.16894662953316)

if __name__ == '__main__':
    calculation().main()