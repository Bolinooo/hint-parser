from src import url
from src import helper
import requests

import unittest

cfg = helper.get_config('config.ini')
sections = cfg.options('OPTIONS')


class MyUrlTest(unittest.TestCase):

    good = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw3/14/t/t00050.htm"
    bad = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw1/14/t/t00050.htm"

    def setUp(self):
        print("Testing method: {0}".format(self._testMethodName[5:]))

    def tearDown(self):
        print("Succesfully tested: {0}".format(self._testMethodName[5:]))

    def test_build_url(self):
        self.assertEqual(
            url.build_url(quarter=3, option='teacher', week=14, num=50), self.__class__.good)
        self.assertNotEqual(
            url.build_url(quarter=3, option='teacher', week=14, num=50), self.__class__.bad)

    def test_get_response(self):
        self.assertTrue(
            url.get_response(self.__class__.good), (requests.get(self.__class__.good), 200))
        self.assertTrue(
            url.get_response(self.__class__.bad), (requests.get(self.__class__.bad), 404))
        self.assertNotEqual(
            url.get_response(self.__class__.good), (requests.get(self.__class__.good), 404))
        self.assertNotEqual(
            url.get_response(self.__class__.bad), (requests.get(self.__class__.bad), 200))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MyUrlTest)
    unittest.TextTestRunner(verbosity=2).run(suite)