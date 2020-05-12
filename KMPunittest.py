import unittest
from KMPalgorithm import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.needle = "abcdefg"
        self.assertEqual(temp.FailureFunction(self.needle),
                         [-1, -1, -1, -1, -1, -1, -1])

    def test_basic_function2(self):
        temp = Solution()
        self.needle = "abcabc"
        self.assertEqual(temp.FailureFunction(
            self.needle), [-1, -1, -1, 0, 1, 2])

    def test_basic_function3(self):
        temp = Solution()
        self.needle = "abababac"
        self.assertEqual(temp.FailureFunction(
            self.needle), [-1, -1, 0, 1, 2, 3, 4, -1])

    def test_basic_function4(self):
        temp = Solution()
        self.needle = "AABAACAABAA"
        self.assertEqual(temp.FailureFunction(
            self.needle), [-1, 0, -1, 0, 1, -1, 0, 1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
