import unittest
from app.io import input


class TestInput(unittest.TestCase):
    def test_read_file(self):
        self.assertRaises(TypeError, input.read_text_from_file, 212)
        self.assertRaises(FileNotFoundError, input.read_text_from_file, "notexists.file")
        expected_contents = ["Hello Antonina"]
        file_contents = input.read_text_from_file("tests/data/testfile.txt")
        self.assertEqual(expected_contents, file_contents)

    def test_pandas_read_file(self):
        self.assertRaises(FileNotFoundError, input.read_text_from_file_with_pandas, "notexists.file")
        self.assertRaises(Exception, input.read_text_from_file_with_pandas, "tests/data/testfile.txt")
        self.assertRaises(TypeError, input.read_text_from_file_with_pandas, 12331)


if __name__ == '__main__':
    unittest.main()
