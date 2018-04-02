from src import helper
from src import url

from datetime import datetime
import unittest
import configparser


class MyHelperTest(unittest.TestCase):

    current = datetime.now()
    time_format = current.strftime('%d-%m')

    def test_get_config(self):
        self.assertEqual(helper.get_config('config.inii'), None)
        self.assertIsInstance(helper.get_config('config.ini'), configparser.ConfigParser)

    def test_apply_format(self):
        self.assertNotEqual(url.apply_format(3), "000003")
        self.assertEqual(url.apply_format(3), "00003")
        self.assertNotEqual(url.apply_format(3), "0003")

    def test_build_filename(self):
        self.assertEqual(helper.build_filename(), 'schedule_' + self.__class__.time_format)


if __name__ == "__main__":
    unittest.main()
