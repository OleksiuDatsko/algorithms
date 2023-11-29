import unittest

from src.string import find_patern


class TestString(unittest.TestCase):
    def test_case_empty_strings(self):
        haystack = ""
        needle = ""
        self.assertEqual([], find_patern(haystack, needle))

    def test_case_empty_needle(self):
        haystack = "abcde"
        needle = ""
        self.assertEqual(list(range(len(haystack))), find_patern(haystack, needle))

    def test_case_empty_haystack(self):
        haystack = ""
        needle = "abc"
        self.assertEqual([], find_patern(haystack, needle))

    def test_case_no_match(self):
        haystack = "abcdef"
        needle = "xyz"
        self.assertEqual([], find_patern(haystack, needle))

    def test_case_single_occurrence(self):
        haystack = "abababc"
        needle = "abc"
        self.assertEqual([4], find_patern(haystack, needle))

    def test_case_multiple_occurrences(self):
        haystack = "abababcababc"
        needle = "abc"
        self.assertEqual([4, 9], find_patern(haystack, needle))

    def test_case_pattern_at_beginning(self):
        haystack = "abcdef"
        needle = "abc"
        self.assertEqual([0], find_patern(haystack, needle))

    def test_case_pattern_at_end(self):
        haystack = "xyzabc"
        needle = "abc"
        self.assertEqual([3], find_patern(haystack, needle))


if __name__ == "__main__":
    unittest.main()
