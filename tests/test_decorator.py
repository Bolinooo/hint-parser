import unittest
import requests

from src import decorator
from src import core


class MyDecorators(unittest.TestCase):

    def test_validate_url(self):
        self.assertEqual(core.get_response("https://www.google.nll"), None)
        self.assertEqual(core.get_response("https://www.google.nl"), 200)


if __name__ == "__main__":
    unittest.main()