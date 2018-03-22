import unittest

from src import helper

class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(helper.fun(3), 4)