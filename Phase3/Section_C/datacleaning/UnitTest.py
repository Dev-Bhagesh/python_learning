from calculator import CalculateAverage
import unittest

class Calculator(unittest.TestCase):

    def hello():
        print('Hello world')

    # def test_equal(self):
    #     try:
    #         self.assertEqual(6,7)
    #     except AssertionError as e:
    #         print('The Assertion error has occured')

    def test_avg(self):
        actual = CalculateAverage(100,10)
        expected = 10

        self.assertEqual(actual,expected)

    def test_zero_avg(self):
        actual = CalculateAverage(100,0)
        expected = 0
        self.assertEqual(expected,actual)

    def test_negative_avg(self):
        actual = CalculateAverage(-100,10)
        expected = -10
        self.assertEqual(expected,actual)


if __name__ == '__main__':
    unittest.main()