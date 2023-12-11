import shutil
import unittest
import os

from src.ijones import ijones


class Testijones(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_temp_directory"
        os.makedirs(self.test_dir, exist_ok=True)

    def test_ijones_ex1(self):
        input_content = "\n".join(
            [
                "3 3",
                "aaa",
                "cab",
                "def",
            ]
        )
        expected_output_content = "5"

        input_filename = os.path.join(self.test_dir, "ijones.in")
        output_filename = os.path.join(self.test_dir, "ijones.out")

        with open(input_filename, "w") as input_file:
            input_file.write(input_content)

        ijones(input_filename, output_filename)

        self.assertTrue(os.path.exists(output_filename))

        with open(output_filename, "r") as output_file:
            actual_output_content = output_file.read()

        self.assertEqual(actual_output_content, expected_output_content)

    def test_ijones_ex2(self):
        input_content = "\n".join(
            [
                "10 1",
                "abcdefaghi",
            ]
        )
        expected_output_content = "2"
        input_filename = os.path.join(self.test_dir, "ijones.in")
        output_filename = os.path.join(self.test_dir, "ijones.out")

        with open(input_filename, "w") as input_file:
            input_file.write(input_content)

        ijones(input_filename, output_filename)

        self.assertTrue(os.path.exists(output_filename))

        with open(output_filename, "r") as output_file:
            actual_output_content = output_file.read()

        self.assertEqual(actual_output_content, expected_output_content)

    def test_ijones_ex3(self):
        input_content = "\n".join(
            [
                "7 6",
                "aaaaaaa",
                "aaaaaaa",
                "aaaaaaa",
                "aaaaaaa",
                "aaaaaaa",
                "aaaaaaa",
            ]
        )
        expected_output_content = "201684"
        input_filename = os.path.join(self.test_dir, "ijones.in")
        output_filename = os.path.join(self.test_dir, "ijones.out")

        with open(input_filename, "w") as input_file:
            input_file.write(input_content)

        ijones(input_filename, output_filename)

        self.assertTrue(os.path.exists(output_filename))

        with open(output_filename, "r") as output_file:
            actual_output_content = output_file.read()

        self.assertEqual(actual_output_content, expected_output_content)

    def tearDown(self):
        shutil.rmtree(self.test_dir)


if __name__ == "__main__":
    unittest.main()
