from src import helper

import unittest
import configparser


class MyHelperTest(unittest.TestCase):

    def test_get_config(self):
        self.assertEqual(helper.get_config('config.inii'), None)
        self.assertIsInstance(helper.get_config('config.ini'), configparser.ConfigParser)


if __name__ == "__main__":
    unittest.main()
