import unittest
from KMPalgorithm import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.needle = "abcdefg"
        self.assertEqual(temp.FailureFunction(self.needle),
                         [0, 0, 0, 0, 0, 0, 0])

    def test_basic_function2(self):
        temp = Solution()
        self.needle = "abcabc"
        self.assertEqual(temp.FailureFunction(
            self.needle), [0, 0, 0, 1, 2, 3])

    def test_basic_function3(self):
        temp = Solution()
        self.needle = "abababac"
        self.assertEqual(temp.FailureFunction(
            self.needle), [0, 0, 1, 2, 3, 4, 5, 0])

    def test_basic_function4(self):
        temp = Solution()
        self.needle = "AABAACAABAA"
        self.assertEqual(temp.FailureFunction(
            self.needle), [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5])

    def test_basic_issip(self):
        temp = Solution()
        self.needle = "issip"
        self.assertEqual(temp.FailureFunction(
            self.needle), [0, 0, 0, 1, 0])


if __name__ == "__main__":
    unittest.main()
