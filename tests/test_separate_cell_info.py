from src import parser
import unittest


class SeparateCellInfoTest(unittest.TestCase):


    def test_teacher(self):
        # correct
        string = "CALDJ"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertEqual(result, {'teacher': string})

        # more than 5 letters
        string = "QWERASS"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'teacher': string})

        # less than 5 letters
        string = "QRASSS"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'teacher': string})

        # 5 characters but not all all letters
        string = "Q?AS1"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'teacher': string})

    def test_lecture(self):
        # correct
        string = "INFSKL04-2"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertEqual(result, {'lecture': string})

        string = "HP-voorlichting"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertEqual(result, {'lecture': string})

        # not enough letters
        string = "INFKL04-2"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'lecture': string})

        # too many letters
        string = "INFSSKL04-2"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'lecture': string})

        # invalid
        string = "INF3A"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'lecture': string})

    # def test_room(self):
    #     # correct
    #     string = "WD.01.003"
    #     dict = {string}
    #     result = parser.separate_cell_info(dict)
    #     self.assertEqual(result, {'room': string})
    #
    #     string = "H.5.314"
    #     dict = {string}
    #     result = parser.separate_cell_info(dict)
    #     self.assertEqual(result, {'room': string})
    #
    #     # not enough letters
    #     string = "H.5.31"
    #     dict = {string}
    #     result = parser.separate_cell_info(dict)
    #     self.assertNotEqual(result, {'room': string})
    #
    #     # too many letters
    #     string = "H.501.314"
    #     dict = {string}
    #     result = parser.separate_cell_info(dict)
    #     self.assertNotEqual(result, {'room': string})
    #
    #     # invalid
    #     string = "Ha5,314"
    #     dict = {string}
    #     result = parser.separate_cell_info(dict)
    #     self.assertNotEqual(result, {'room': string})

    def test_lecture_number(self):
        # correct
        string = "1"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertEqual(result, {'lecture_number': string})

        string = "1234"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertEqual(result, {'lecture_number': string})

        # invalid
        string = "1-a?"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'lecture_number': string})

        # too many
        string = "a12333"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'lecture_number': string})

        # invalid
        string = "-123"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'lecture_number': string})

    def test_extra_info(self):
        # correct
        string = "1)"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertEqual(result, {'extra_info': string})

        # too many
        string = "a12333"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'extra_info': string})

        # invalid
        string = "-123"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'extra_info': string})

    def test_class(self):
        # correct
        string = "1)"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertEqual(result, {'extra_info': string})

        # too many
        string = "a12333"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'extra_info': string})

        # invalid
        string = "-123"
        dict = {string}
        result = parser.separate_cell_info(dict)
        self.assertNotEqual(result, {'extra_info': string})
# if __name__ == "__main__":
#     unittest.main()
