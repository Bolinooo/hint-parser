from src import core

import requests
import unittest


class MyDecoratorTests(unittest.TestCase):

    def test_validate_url(self):
        self.assertEqual(core.get_response("https://www.google.nll"), None)
        self.assertIsInstance(core.get_response("https://www.google.nl"), tuple)


if __name__ == "__main__":
    unittest.main()
