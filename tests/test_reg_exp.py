from src import reg_ex_patterns as reg

import unittest
import re


def pattern_test_helper(list, pattern):
    """
    Function to facilitate the tests in MyRegExTest class
    :param list: list with strings of cases that should be tested
    :param pattern: a regular expression
    :return: list with the result of all matches
    """
    newList = []
    for item in list:
        matched = re.match(pattern, item)
        if (matched == None):
            raise ValueError(item + ' does not match the pattern')
        newList.append(matched.group())
    return newList

# tests are done with multiple correct cases and incorrect cases
class MyRegExTest(unittest.TestCase):
    def test_teacher(self):
        list = ["ABBAM", "AMIGA", "MINUA"]
        matches = pattern_test_helper(list, reg.teacher_pattern)
        self.assertEqual(list, matches)

        # not 5 letters
        fail = "INF1G"
        m = re.match(reg.teacher_pattern, fail)
        self.assertEqual(m, None)
        # too long
        fail = "ABBAMQ"
        m = re.match(reg.teacher_pattern, fail)
        self.assertEqual(m, None)
        # too short
        fail = "ABBA"
        m = re.match(reg.teacher_pattern, fail)
        self.assertEqual(m, None)

    def test_extra_info(self):
        list = ["1)", "9)"]
        matches = pattern_test_helper(list, reg.extra_info_pattern)
        self.assertEqual(list, matches)
        # not single digit)
        fail = "ABBAM"
        m = re.match(reg.extra_info_pattern, fail)
        self.assertEqual(m, None)
        # not single digit)
        fail = "11)"
        m = re.match(reg.extra_info_pattern, fail)
        self.assertEqual(m, None)

    def test_lecture1(self):
        list = ["INFANL02-3", "TINPRJ0178", "CCOCKE10R3", "INFLAB01"]
        matches = pattern_test_helper(list, reg.lecture_pattern1)
        self.assertEqual(list, matches)
        # not a lecture but a teacher
        fail = "ABBAM"
        m = re.match(reg.lecture_pattern1, fail)
        self.assertEqual(m, None)
        # not a lecture but a class
        fail = "MINBOD02"
        m = re.match(reg.lecture_pattern1, fail)
        self.assertEqual(m, None)

    def test_lecture2(self):
        list = ["CMD-DC01-3"]
        matches = pattern_test_helper(list, reg.lecture_pattern2)
        self.assertEqual(list, matches)

        # not a lecture but a teacher
        fail = "ABBAM"
        m = re.match(reg.lecture_pattern2, fail)
        self.assertEqual(m, None)
        # not a lecture but a class
        fail = "MINBOD02"
        m = re.match(reg.lecture_pattern2, fail)
        self.assertEqual(m, None)

    def test_lecture_specific(self):
        list = ["HP-voorlichting"]
        matches = pattern_test_helper(list, reg.lecture_specific)
        self.assertEqual(list, matches)

        # not a lecture but a teacher
        fail = "ABBAM"
        m = re.match(reg.lecture_specific, fail)
        self.assertEqual(m, None)
        # not a lecture but a class
        fail = "INF2D"
        m = re.match(reg.lecture_specific, fail)
        self.assertEqual(m, None)

    def test_location(self):
        list = ["WD.01.003", "H.5.314"]
        matches = pattern_test_helper(list, reg.location_pattern)
        self.assertEqual(list, matches)

        special = "H.5.314, H"
        m = re.match(reg.location_pattern, special)
        self.assertEqual(m.group(), "H.5.314")

        # too short
        fail = "WD.1.1"
        m = re.match(reg.location_pattern, fail)
        self.assertEqual(m, None)
        # not a location but a class
        fail = "INF2D"
        m = re.match(reg.location_pattern, fail)
        self.assertEqual(m, None)

    def test_lecture_number(self):
        list = ["1", "1800", "2368"]
        matches = pattern_test_helper(list, reg.lecture_number_pattern)
        self.assertEqual(list, matches)

        # too short
        fail = "WD.1.1"
        m = re.match(reg.location_pattern, fail)
        self.assertEqual(m, None)
        # not a lecture but a class
        fail = "INF2D"
        m = re.match(reg.location_pattern, fail)
        self.assertEqual(m, None)

    def test_class1(self):
        list = ["COD2", "COV1D", "INF2D", "DCMD1A", "DINF1", "CMD1A", "TI1A"]
        matches = pattern_test_helper(list, reg.class_pattern1)
        self.assertEqual(list, matches)

        # too short
        fail = "C2"
        m = re.match(reg.class_pattern1, fail)
        self.assertEqual(m, None)
        # starts with a number instead of a letter
        fail = "2NF2D"
        m = re.match(reg.class_pattern1, fail)
        self.assertEqual(m, None)

    def test_class2(self):
        list = ["BO-COM", "BO-TI", "CMD-BO", "COD-AD3", "CMD-DT01-6", "CMT-BO", "COV3-HP"]
        matches = pattern_test_helper(list, reg.class_pattern2)
        self.assertEqual(list, matches)

        # too short
        fail = "B-COM"
        m = re.match(reg.class_pattern2, fail)
        self.assertEqual(m, None)
        # starts with a number instead of a letter
        fail = "2B-COM"
        m = re.match(reg.class_pattern2, fail)
        self.assertEqual(m, None)

    def test_class3(self):
        list = ["MINBOD02A", "MINBOD02", "MINIED1C", "MIN ENS02", "MIN IED1B", "MIN SMO", "KEU AAR01", "KEU SOU01K"]
        matches = pattern_test_helper(list, reg.class_pattern3)
        self.assertEqual(list, matches)

        # too short
        fail = "MINBD02"
        m = re.match(reg.class_pattern3, fail)
        self.assertEqual(m, None)
        # starts with a number instead of a letter
        fail = "2INBOD02A"
        m = re.match(reg.class_pattern3, fail)
        self.assertEqual(m, None)

    def test_class_cmd_lab(self):
        list = ["CMDLABEXP", "CMDLABPT"]
        matches = pattern_test_helper(list, reg.class_cmd_lab_pattern)
        self.assertEqual(list, matches)

        # too short
        fail = "CMDLABQ"
        m = re.match(reg.class_cmd_lab_pattern, fail)
        self.assertEqual(m, None)
        # doesnt start with cmd
        fail = "2MDLABEXP"
        m = re.match(reg.class_cmd_lab_pattern, fail)
        self.assertEqual(m, None)

    def test_class_specific(self):
        list = ["cmd", "marjo", "opbouw", "overloop", "RESCMD", "TENT", "uitloop lokaal"]
        matches = pattern_test_helper(list, reg.class_specific_pattern)
        self.assertEqual(list, matches)
        # not in the list
        fail = "AMIGA"
        m = re.match(reg.class_cmd_lab_pattern, fail)
        self.assertEqual(m, None)
