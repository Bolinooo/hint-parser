from src import helper
from src import url
import calendar
import time
import unittest


class MyHelperTest(unittest.TestCase):

    timestamp = calendar.timegm(time.gmtime())

    def setUp(self):
        print("Testing method: {0}".format(self._testMethodName))

    def tearDown(self):
        print("Succesfully tested: {0}".format(self._testMethodName))

    def test_apply_format(self):
        self.assertNotEqual(url.apply_format(3), "000003")
        self.assertEqual(url.apply_format(3), "00003")
        self.assertNotEqual(url.apply_format(3), "0003")

    def test_build_filename_teacher(self):
        self.assertNotEqual(helper.build_filename(option="teacher", quarter="1"), 'teacher_q2_' + str(self.__class__.timestamp))
        self.assertEqual(helper.build_filename(option="teacher", quarter="2"), 'teacher_q2_' + str(self.__class__.timestamp))
        self.assertNotEqual(helper.build_filename(option="teacher", quarter="3"), 'teacher_q2_' + str(self.__class__.timestamp))

    def test_build_filename_rooms(self):
        self.assertNotEqual(helper.build_filename(option="rooms", quarter="1"), 'rooms_q2_' + str(self.__class__.timestamp))
        self.assertEqual(helper.build_filename(option="rooms", quarter="2"), 'rooms_q2_' + str(self.__class__.timestamp))
        self.assertNotEqual(helper.build_filename(option="rooms", quarter="3"), 'rooms_q2_' + str(self.__class__.timestamp))

    def test_build_filename_schedule(self):
        self.assertNotEqual(helper.build_filename(option="schedule", quarter="1"), 'schedule_q2_' + str(self.__class__.timestamp))
        self.assertEqual(helper.build_filename(option="schedule", quarter="2"), 'schedule_q2_' + str(self.__class__.timestamp))
        self.assertNotEqual(helper.build_filename(option="schedule", quarter="3"), 'schedule_q2_' + str(self.__class__.timestamp))

    def test_build_filename_classes(self):
        self.assertNotEqual(helper.build_filename(option="classes", quarter="1"), 'classes_q2_' + str(self.__class__.timestamp))
        self.assertEqual(helper.build_filename(option="classes", quarter="2"), 'classes_q2_' + str(self.__class__.timestamp))
        self.assertNotEqual(helper.build_filename(option="classes", quarter="3"), 'classes_q2_' + str(self.__class__.timestamp))


if __name__ == "__main__":
    unittest.main()
