from src import helper
from src import url

from datetime import datetime
import unittest
import configparser
import os


class MyHelperTest(unittest.TestCase):

    current = datetime.now()
    time_format = current.strftime('%d-%m')
    test_dict = {"key1": {"key2": {"key3": "value1"}}}

    def setUp(self):
        print("Testing method: {0}".format(self._testMethodName))

    def tearDown(self):
        print("Succesfully tested: {0}".format(self._testMethodName))

    def test_get_config(self):
        self.assertEqual(helper.get_config('config.inii'), None)
        self.assertIsInstance(helper.get_config('config.ini'), configparser.ConfigParser)

    def test_apply_format(self):
        self.assertNotEqual(url.apply_format(3), "000003")
        self.assertEqual(url.apply_format(3), "00003")
        self.assertNotEqual(url.apply_format(3), "0003")

    def test_build_filename(self):
        self.assertEqual(helper.build_filename(), 'schedule_' + self.__class__.time_format)

    def test_convert_json(self):
        helper.convert_json(self.__class__.test_dict)
        self.assertTrue(os.path.isfile('{0}.json'.format('schedule_' + self.__class__.time_format)), True)


if __name__ == "__main__":
    unittest.main()
