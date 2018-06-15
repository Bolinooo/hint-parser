from bs4 import BeautifulSoup
from src import parser
import requests
import unittest


class MyParserTest(unittest.TestCase):
    url = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw3/16/t/t00050.htm"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    date = soup.find_all('font')[-1].get_text(strip=True)

    def setUp(self):
        print("Testing method: {0}".format(self._testMethodName))

    def tearDown(self):
        print("Succesfully tested: {0}".format(self._testMethodName))

    def test_convert_date(self):
        self.assertNotEqual(parser.convert_date(self.__class__.date, 1), ('Zondag', '2018-04-15'))
        self.assertNotEqual(parser.convert_date(self.__class__.date, 1), ('Maandag', '2018-04-15'))
        self.assertEqual(parser.convert_date(self.__class__.date, 1), ('Maandag', '2018-04-16'))
        self.assertNotEqual(parser.convert_date(self.__class__.date, 1), ('Maandag', '2018-04-17'))
        self.assertNotEqual(parser.convert_date(self.__class__.date, 1), ('Dinsdag', '2018-04-17'))

        self.assertNotEqual(parser.convert_date(self.__class__.date, 5), ('Donderdag', '2018-04-19'))
        self.assertNotEqual(parser.convert_date(self.__class__.date, 5), ('Vrijdag', '2018-04-19'))
        self.assertEqual(parser.convert_date(self.__class__.date, 5), ('Vrijdag', '2018-04-20'))
        self.assertNotEqual(parser.convert_date(self.__class__.date, 5), ('Vrijdag', '2018-04-21'))
        self.assertNotEqual(parser.convert_date(self.__class__.date, 5), ('Zaterdag', '2018-04-21'))

    def test_convert_timetable(self):
        self.assertNotEqual(parser.convert_timetable(1, 3), ('8:30', '9:20', '09:20', '10:30'))
        self.assertEqual(parser.convert_timetable(1, 3), ('8:30', '9:20', '10:30', '11:20'))
        self.assertNotEqual(parser.convert_timetable(1, 3), ('8:30', '9:20', '11:20', '12:10'))

    def test_seperate_cell_info(self):
        """
        Tables cells are replicated with an array called iterator.
        Firstly, 3 valid cases (cells with certain info) will be tested if this function works correctly.
        Afterwards, 1 weird case will be tested
        """
        item1 = "-3"
        iterator = [item1]
        new_dict = parser.get_separated_cell_info(iterator)
        self.assertEqual(new_dict, {"event": item1})

        building = "H"
        floor = "5"
        room = "314"
        item1 = building + "." + floor + "." + room
        iterator = [item1]
        new_dict = parser.get_separated_cell_info(iterator)
        self.assertEqual(new_dict, {"building": building,
                                    "floor": floor,
                                    "room": room
                                    })

        building = "WD"
        floor = "04"
        room = "002"
        item1 = "INFANL02-3"
        item2 = "INF1I"
        item3 = building + "." + floor + "." + room
        item4 = "492"
        item5 = "4)"
        iterator = [item1, item2, item3, item4, item5]
        new_dict = parser.get_separated_cell_info(iterator)
        self.assertEqual(new_dict,
                         {"lecture": item1,
                          "class": item2,
                          "building": building,
                          "floor": floor,
                          "room": room,
                          "lecture_nr": item4,
                          "extra_info": item5
                          })
        """
        Building can not be W2D so item3 will become an event instead.
        """
        building = "W2D"
        floor = "04"
        room = "002"
        item1 = "INFANL02-3"
        item2 = "INF1I"
        item3 = building + "." + floor + "." + room
        iterator = [item1, item2, item3]
        new_dict = parser.get_separated_cell_info(iterator)
        self.assertEqual(new_dict,
                         {"lecture": item1,
                          "class": item2,
                          "event": item3
                          })

        building = "H"
        floor = "5"
        room = "314"
        item1 = building + "." + floor + "." + room
        iterator = [item1]
        new_dict = parser.get_separated_cell_info(iterator)
        self.assertNotEqual(new_dict, {"lecture": item1 })

    def test_get_category_and_result(self):
        input = "INF2D"
        category = "class"
        data = parser.get_category_and_result(input)
        self.assertEqual(data[0], category)
        self.assertEqual(data[1], input)

        input = "AMIG"
        data = parser.get_category_and_result(input)
        self.assertEqual(data, None)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MyParserTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
