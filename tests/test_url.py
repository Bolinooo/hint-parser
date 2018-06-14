from src import url
import requests
import unittest


class MyUrlTest(unittest.TestCase):

    good_teacher = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw4/24/t/t00104.htm"
    bad_teacher = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw4/14/t/t00104.htm"

    good_class = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw4/24/c/c00093.htm"
    bad_class = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw4/1/c/c00093.htm"

    good_rooms = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw4/24/r/r00003.htm"
    bad_rooms = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw4/14/r/r00003.htm"



    settings = {
        'teacher': 't',
        'schedule': 'c',
        'classes': 'c',
        'rooms': 'r',
        'base_url': "http://misc.hro.nl/roosterdienst/webroosters/",
        'teacher_items': ['title_blue', 'title_black'],
    }

    def setUp(self):
        print("Testing method: {0}".format(self._testMethodName))

    def tearDown(self):
        print("Succesfully tested: {0}".format(self._testMethodName))

    def test_build_url_teacher(self):
        self.assertEqual(
            url.build_url(settings=self.__class__.settings, quarter=4, option='teacher', week=24, num=104), self.good_teacher)
        self.assertNotEqual(
            url.build_url(settings=self.__class__.settings, quarter=4, option='teacher', week=50, num=104), self.bad_teacher)

    def test_get_response_teacher(self):
        self.assertTrue(
            url.get_response(self.good_teacher), (requests.get(self.good_teacher), 200))
        self.assertTrue(
            url.get_response(self.bad_teacher), (requests.get(self.bad_teacher), 404))
        self.assertNotEqual(
            url.get_response(self.good_teacher), (requests.get(self.good_teacher), 404))
        self.assertNotEqual(
            url.get_response(self.bad_teacher), (requests.get(self.bad_teacher), 200))

    def test_build_url_class(self):
        self.assertEqual(
            url.build_url(settings=self.__class__.settings, quarter=4, option='classes', week=24, num=93), self.good_class)
        self.assertNotEqual(
            url.build_url(settings=self.__class__.settings, quarter=4, option='classes', week=50, num=104), self.bad_class)

    def test_get_response_class(self):
        self.assertTrue(
            url.get_response(self.good_class), (requests.get(self.good_class), 200))
        self.assertTrue(
            url.get_response(self.bad_class), (requests.get(self.bad_class), 404))
        self.assertNotEqual(
            url.get_response(self.good_class), (requests.get(self.good_class), 404))
        self.assertNotEqual(
            url.get_response(self.bad_class), (requests.get(self.bad_class), 200))


    def test_build_url_rooms(self):
        self.assertEqual(
            url.build_url(settings=self.__class__.settings, quarter=4, option='rooms', week=24, num=3),
            self.good_rooms)
        self.assertNotEqual(
            url.build_url(settings=self.__class__.settings, quarter=4, option='rooms', week=50, num=3),
            self.bad_rooms)

    def test_get_response_rooms(self):
        self.assertTrue(
            url.get_response(self.good_rooms), (requests.get(self.good_rooms), 200))
        self.assertTrue(
            url.get_response(self.bad_rooms), (requests.get(self.bad_rooms), 404))
        self.assertNotEqual(
            url.get_response(self.good_rooms), (requests.get(self.good_rooms), 404))
        self.assertNotEqual(
            url.get_response(self.bad_rooms), (requests.get(self.bad_rooms), 200))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MyUrlTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
