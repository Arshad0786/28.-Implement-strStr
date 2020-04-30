import unittest
from ImplementstrStr import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.heystack = "hello"
        self.needle = "ll"
        self.assertEqual(temp.strStr(self.heystack,self.needle), 2)


if __name__ == "__main__":
    unittest.main()
