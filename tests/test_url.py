from src import url
import unittest


class MyUrlTest(unittest.TestCase):

    def test_build_dict(self):
        self.assertEqual(url.build_dict(), type(dict))


if __name__ == "__main__":
    unittest.main()
