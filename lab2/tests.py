import unittest

from hamsters_v3 import get_number_of_hamsters


class TestGetNumberOfHamsters(unittest.TestCase):
    def test_get_number_of_hamsters_s7_c3(self):
        hamsters = [
            [1, 2],
            [2, 2],
            [3, 1],
        ]
        s = 7
        c = 3
        self.assertEqual(get_number_of_hamsters(s, c, hamsters), 2)

    def test_get_number_of_hamsters_s19_c4(self):
        hamsters = [
            [5, 0],
            [2, 2],
            [1, 4],
            [5, 1],
        ]
        s = 19
        c = 4
        self.assertEqual(get_number_of_hamsters(s, c, hamsters), 3)

    def test_get_number_of_hamsters_s2_c2(self):
        hamsters = [
            [1, 50000],
            [1, 60000],
        ]
        s = 2
        c = 2
        self.assertEqual(get_number_of_hamsters(s, c, hamsters), 1)
        
    def test_get_number_of_hamsters_s9_c4(self):
        hamsters = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            ]
        s = 9
        c = 4
        self.assertEqual(get_number_of_hamsters(s, c, hamsters), 1)


if __name__ == "__main__":
    unittest.main()
