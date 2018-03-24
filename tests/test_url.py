from src import url
import unittest


class MyUrlTest(unittest.TestCase):

    def test_build_sequence(self):
        self.assertEqual(url.build_sequence(3),({"000001", "000002", "000003"}))


if __name__ == "__main__":
    unittest.main()
