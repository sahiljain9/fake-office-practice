
import unittest

from src.average import calculate_average


class TestCalculateAverage(unittest.TestCase):

    # Test 1: Normal positive numbers
    def test_positive_numbers(self):
        result = calculate_average(10, 20, 30)
        self.assertEqual(result, 20.0)

    # Test 2: All numbers are zero
    def test_zero_values(self):
        result = calculate_average(0, 0, 0)
        self.assertEqual(result, 0.0)

    # Test 3: Negative numbers
    def test_negative_numbers(self):
        result = calculate_average(-10, -20, -30)
        self.assertEqual(result, -20.0)

    # Test 4: Decimal numbers
    def test_decimal_numbers(self):
        result = calculate_average(1.5, 2.5, 3.5)
        self.assertAlmostEqual(result, 2.5)

    # Test 5: Mixed positive and negative numbers
    def test_mixed_numbers(self):
        result = calculate_average(-10, 10, 30)
        self.assertAlmostEqual(result, 10.0)


if __name__ == "__main__":
    unittest.main()
