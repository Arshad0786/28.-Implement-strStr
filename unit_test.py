import unittest
from ImplementstrStr import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.heystack = "hello"
        self.needle = "ll"
        self.assertEqual(temp.strStr(self.heystack,self.needle), 2)

    def test_no_needle_found(self):
        temp = Solution()
        self.heystack = "HelloWorld"
        self.needle = "aa"
        self.assertEqual(temp.strStr(self.heystack,self.needle), -1)

    def test_haystack_is_needle(self):
        temp = Solution()
        self.heystack = "needle"
        self.needle = "needle"
        self.assertEqual(temp.strStr(self.heystack,self.needle), 0)

    def test_empty_needle(self):
        temp = Solution()
        self.heystack = "aword"
        self.needle = ""
        self.assertEqual(temp.strStr(self.heystack,self.needle), 0)

    def test_needle_in_the_front(self):
        temp = Solution()
        self.heystack = "aabbccdd"
        self.needle = "aa"
        self.assertEqual(temp.strStr(self.heystack,self.needle), 0)

    def test_needle_in_the_end(self):
        temp = Solution()
        self.heystack = "aabbccdd"
        self.needle = "dd"
        self.assertEqual(temp.strStr(self.heystack,self.needle), 6)

    def test_needle_in_the_middle(self):
        temp = Solution()
        self.heystack = "aabbccddee"
        self.needle = "cc"
        self.assertEqual(temp.strStr(self.heystack,self.needle), 4)

    def test_needle_larger_than_haystack(self):
        temp = Solution()
        self.heystack = "aaa"
        self.needle = "aaaa"
        self.assertEqual(temp.strStr(self.heystack,self.needle), -1)

    def test_needle_euqal_last_letter(self):
        temp = Solution()
        self.heystack = "abcdefg"
        self.needle = "gigeo"
        self.assertEqual(temp.strStr(self.heystack,self.needle), -1)


if __name__ == "__main__":
    unittest.main()
