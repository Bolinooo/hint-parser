from src import url
import unittest


class MyUrlTest(unittest.TestCase):

    def test_build_dict(self):
        self.assertIsInstance(url.build_dict(), dict)


if __name__ == "__main__":
    unittest.main()
