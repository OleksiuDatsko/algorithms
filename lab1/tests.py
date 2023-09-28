import unittest

from zig_zag_path import generate_matrix, zig_zag_path


def get_zig_zag_result(n, m):
    return zig_zag_path(generate_matrix(n, m))


class TestZigZagPath(unittest.TestCase):
    def test_zig_zag_path_n5_m5(self):
        zig_zag_result = get_zig_zag_result(n=5, m=5)
        self.assertEqual(
            zig_zag_result,
            [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8],
        )

    def test_zig_zag_path_n4_m2(self):
        zig_zag_result = get_zig_zag_result(n=4, m=2)
        self.assertEqual(
            zig_zag_result,
            [0, 1, 1, 2, 2, 3, 3, 4],
        )

    def test_zig_zag_path_n1_m6(self):
        zig_zag_result = get_zig_zag_result(n=1, m=6)
        self.assertEqual(
            zig_zag_result,
            [0, 1, 2, 3, 4, 5],
        )

    def test_zig_zag_path_n1_m1(self):
        zig_zag_result = get_zig_zag_result(n=1, m=1)
        self.assertEqual(
            zig_zag_result,
            [0],
        )

    def test_zig_zag_path_n0_m0(self):
        zig_zag_result = get_zig_zag_result(n=0, m=0)
        self.assertEqual(
            zig_zag_result,
            [],
        )


if __name__ == "__main__":
    unittest.main()
