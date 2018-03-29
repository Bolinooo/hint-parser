from src import url
from collections import defaultdict

import unittest


class MyUrlTest(unittest.TestCase):

    def test_build_urls(self):
        self.assertEqual(url.build_urls('TEACHER'), defaultdict(list))


if __name__ == "__main__":
    unittest.main()
