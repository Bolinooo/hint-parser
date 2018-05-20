from src import helper
from src import url
import calendar
import time
import unittest


class MyHelperTest(unittest.TestCase):

    timestamp = calendar.timegm(time.gmtime())

    test_dict = {"key1": {"key2": {"key3": "value1"}}}

    def setUp(self):
        print("Testing method: {0}".format(self._testMethodName))

    def tearDown(self):
        print("Succesfully tested: {0}".format(self._testMethodName))

    def test_apply_format(self):
        self.assertNotEqual(url.apply_format(3), "000003")
        self.assertEqual(url.apply_format(3), "00003")
        self.assertNotEqual(url.apply_format(3), "0003")

    def test_build_filename(self):
        self.assertEqual(helper.build_filename(option="teacher", quarter="1"), 'teacher_q1_' + str(self.__class__.timestamp))


if __name__ == "__main__":
    unittest.main()
