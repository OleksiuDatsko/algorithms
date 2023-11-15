import shutil
import unittest
import os

from src.gamsrv import gamsrv


class TestGamsrv(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_temp_directory"
        os.makedirs(self.test_dir, exist_ok=True)

    def test_gamsrv_ex1(self):
        input_content = "\n".join(
            [
                "6 6",
                "1 2 6",
                "1 3 10",
                "3 4 80",
                "4 5 50",
                "5 6 20",
                "2 3 40",
                "2 4 100",
            ]
        )
        expected_output_content = "100"

        input_filename = os.path.join(self.test_dir, "gamsrv.in")
        output_filename = os.path.join(self.test_dir, "gamsrv.out")

        with open(input_filename, "w") as input_file:
            input_file.write(input_content)

        gamsrv(input_filename, output_filename)
        

        self.assertTrue(os.path.exists(output_filename))

        with open(output_filename, "r") as output_file:
            actual_output_content = output_file.read()

        self.assertEqual(actual_output_content, expected_output_content)

    def test_gamsrv_ex2(self):
        input_content = "\n".join(
            [
                "9 12",
                "2 4 6",
                "1 2 20",
                "2 3 20",
                "3 6 20",
                "6 9 20",
                "9 8 20",
                "8 7 20",
                "7 4 20",
                "4 1 20",
                "5 2 10",
                "5 4 10",
                "5 6 10",
                "5 8 10",
            ]
        )
        expected_output_content = "10"
        input_filename = os.path.join(self.test_dir, "gamsrv.in")
        output_filename = os.path.join(self.test_dir, "gamsrv.out")

        with open(input_filename, "w") as input_file:
            input_file.write(input_content)

        gamsrv(input_filename, output_filename)
        

        self.assertTrue(os.path.exists(output_filename))

        with open(output_filename, "r") as output_file:
            actual_output_content = output_file.read()

        self.assertEqual(actual_output_content, expected_output_content)

    def test_gamsrv_ex3(self):
        input_content = "\n".join(
            [
                "3 2",
                "1 3",
                "1 2 50",
                "2 3 1000000000",
            ]
        )
        expected_output_content = "1000000000"
        input_filename = os.path.join(self.test_dir, "gamsrv.in")
        output_filename = os.path.join(self.test_dir, "gamsrv.out")

        with open(input_filename, "w") as input_file:
            input_file.write(input_content)

        gamsrv(input_filename, output_filename)
        

        self.assertTrue(os.path.exists(output_filename))

        with open(output_filename, "r") as output_file:
            actual_output_content = output_file.read()

        self.assertEqual(actual_output_content, expected_output_content)

    def tearDown(self):
        shutil.rmtree(self.test_dir)


if __name__ == "__main__":
    unittest.main()
