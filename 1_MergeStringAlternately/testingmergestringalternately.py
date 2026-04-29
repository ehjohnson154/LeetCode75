
import unittest
from mergestringalternately import Solution


class TestMergeStringAlternately(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_equal_length_strings(self):
        self.assertEqual(
            self.solution.mergeAlternately("abc", "xyz"),
            "axbycz"
        )

    def test_first_string_longer(self):
        self.assertEqual(
            self.solution.mergeAlternately("abcd", "xy"),
            "axbycd"
        )

    def test_second_string_longer(self):
        self.assertEqual(
            self.solution.mergeAlternately("ab", "wxyz"),
            "awbxyz"
        )

    def test_empty_strings(self):
        self.assertEqual(
            self.solution.mergeAlternately("", ""),
            ""
        )
        self.assertEqual(
            self.solution.mergeAlternately("abc", ""),
            "abc"
        )
        self.assertEqual(
            self.solution.mergeAlternately("", "xyz"),
            "xyz"
        )


if __name__ == "__main__":
    unittest.main()