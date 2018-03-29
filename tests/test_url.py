from src import url
from src import helper
from collections import defaultdict

import unittest

cfg = helper.get_config('config.ini')
sections = cfg.options('OPTIONS')


class MyUrlTest(unittest.TestCase):

    def test_build_urls(self):
        self.assertEqual(url.build_urls(sections[0]), defaultdict(list))


if __name__ == "__main__":
    unittest.main()
