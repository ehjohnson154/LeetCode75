import unittest
from gcd_strings import Solution


class testing_gcd_strings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_shared_string(self):
        self.assertEqual(
            self.solution.gcdOfStrings("abc", "abcabc"),
            "abc"
        )

    def test_triplicate_string(self):
        self.assertEqual(
            self.solution.gcdOfStrings("ababababababab", "abab"),
            "ab"
        )
    def test_no_shared_string(self):
        self.assertEqual(
            self.solution.gcdOfStrings("beet", "leet"),
            ""
        )
    def test_no_shared_letters(self):
        self.assertEqual(
            self.solution.gcdOfStrings("abc", "xyz"),
            ""
        )
    def test_almost_divisible(self):
        self.assertEqual(
            self.solution.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"),
            "TAUXX"
        )

    def test_trick(self):
        self.assertEqual(
            self.solution.gcdOfStrings("AAAAAB", "AAA"),
            ""
        )

if __name__ == "__main__":
    unittest.main()

