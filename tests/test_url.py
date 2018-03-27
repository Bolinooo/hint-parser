from src import url
from collections import defaultdict

import unittest


class MyUrlTest(unittest.TestCase):

    def test_build_dict(self):
        self.assertEqual(url.build_dict(), defaultdict(list))


if __name__ == "__main__":
    unittest.main()
