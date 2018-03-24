from src import main

import requests
import unittest


class MyDecoratorTests(unittest.TestCase):

    def test_validate_url(self):
        self.assertEqual(main.get_response("https://www.google.nll"), -1)
        self.assertIsInstance(main.get_response("https://www.google.nl"), tuple)


if __name__ == "__main__":
    unittest.main()
