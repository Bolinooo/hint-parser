from src import url
import unittest


class MyUrlTest(unittest.TestCase):

    def test_apply_format(self):
        self.assertNotEqual(url.apply_format(3), "000003")
        self.assertEqual(url.apply_format(3), "00003")
        self.assertNotEqual(url.apply_format(3), "0003")


if __name__ == "__main__":
    unittest.main()
