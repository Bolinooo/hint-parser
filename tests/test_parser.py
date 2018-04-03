from bs4 import BeautifulSoup
from src import parser
import requests
import unittest


class MyParserTest(unittest.TestCase):

    url = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw3/14/t/t00050.htm"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    date = soup.find_all('font')[-1].get_text(strip=True)

    def setUp(self):
        print("Testing method: {0}".format(self._testMethodName))

    def tearDown(self):
        print("Succesfully tested: {0}".format(self._testMethodName))

    def test_convert_date(self):
        self.assertNotEqual(parser.convert_date(self.__class__.date, 1), ('Dinsdag', '2018-04-02'))
        self.assertEqual(parser.convert_date(self.__class__.date, 1), ('Maandag', '2018-04-02'))
        self.assertEqual(parser.convert_date(self.__class__.date, 5), ('Vrijdag', '2018-04-06'))
        self.assertNotEqual(parser.convert_date(self.__class__.date, 5), ('Vrijdag', '2018-04-07'))

    def test_convert_timetable(self):
        self.assertNotEqual(parser.convert_timetable(1, 3), ('8:30', '9:20', '09:20', '10:30'))
        self.assertEqual(parser.convert_timetable(1, 3), ('8:30', '9:20', '10:30', '11:20'))
        self.assertNotEqual(parser.convert_timetable(1, 3), ('8:30', '9:20', '11:20', '12:10'))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MyParserTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
