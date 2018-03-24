from src import url
import unittest


class MyUrlTest(unittest.TestCase):

    def test_build_sequence(self):
        self.assertEqual(url.apply_format(3), "000003")
        self.assertNotEqual(url.apply_format(3), "00003")


if __name__ == "__main__":
    unittest.main()
