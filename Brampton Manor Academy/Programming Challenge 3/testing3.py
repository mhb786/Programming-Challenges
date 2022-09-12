from 99_trick import calculation_result


class MyFirstTests(calculation_result.TestCase):

    def test_calculation(self):
        self.assertEqual(calculation(answer, factor), 15)

if __name__ == '__main__':
    calculation_result.main()