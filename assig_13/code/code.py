########################################################################
 ##
 ## CS 101 Lab
 ## Program 13
 ## Name: Osay E
 ## Email: ooenw7@umsystem.edu
 ##
 ##      Step 1: Define functions
 ##      Step 2: Call unittest.main()
 ##      Step 3: End
 ##ERROR HANDLING
 ##      N/A
 ##
 ## OTHER COMMENTS:
 ##      Any special comments
 ##
 ########################################################################
import math
import unittest
import grade
class grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = grade.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")
    def test_total_returns_0(self):
        result = grade.total([])
        self.assertEqual(result, 0, "The total function should return 0")
    def test_average_one(self):
        result = grade.average([2, 5, 9])
        self.assertAlmostEqual(result, 5.33333, 5, "The average should return 5.33333")
    def test_average_two(self):
        result = grade.average([2, 15, 22, 9])
        self.assertAlmostEqual(result, 12.0000, 4, "The average should return 12")
    def test_average_returns_nan(self):
        result = grade.average([])
        self.assertIs(result, math.nan, "The average should return nan")
    def test_median_returns_one(self):
        result = grade.median([2, 5, 1])
        self.assertEqual(result, 2, "The median should return 2")
    def test_median_returns_two(self):
        result = grade.median([5, 2, 1, 3])
        self.assertAlmostEqual(result, 2.5, 1, "The median should return 2.5")
    def test_median_raise_error(self):
        with self.assertRaises(ValueError):
            result = grade.median([])
            return result
if __name__ == "__main__":
    unittest.main()