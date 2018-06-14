from src import regex_patterns as reg

import unittest
import re


def test_valid_patterns(list, pattern):
    """
    Function to facilitate the tests in MyRegExTest class
    :param list: list with strings of valid cases
    :param pattern: a regular expression
    :return: list with the result of all matches
    """
    newList = []
    for item in list:
        matched = re.match(pattern, item)
        if matched is None:
            raise ValueError(item + ' does not match the pattern ' + pattern)
        newList.append(matched.group())
    return newList


def test_invalid_patterns(list, pattern):
    """
    Function to facilitate the tests in MyRegExTest class
    :param list: list with strings of invalid cases
    :param pattern: a regular expression
    :return: list with the result of all matches which should be a list of None
    """
    newList = []
    for item in list:
        matched = re.match(pattern, item)
        if matched is None:
            newList.append(None)
        else:
            raise ValueError(item + ' matched to ' + pattern + ' while it should not have matched')

    return newList


# tests are done with multiple correct cases and incorrect cases
class MyRegExTest(unittest.TestCase):
    def test_teacher(self):
        list = ["ABBAM", "AMIGA", "MINUA"]
        matches = test_valid_patterns(list, reg.teacher_pattern)
        self.assertEqual(list, matches)

        # not 5 letters, too long, too short
        list2 = ["INF1G", "ABBAMQ", "ABBA"]
        noMatchesExpectation = [None, None, None]
        noMatches = test_invalid_patterns(list2, reg.teacher_pattern)
        self.assertEqual(noMatchesExpectation, noMatches)

    def test_extra_info(self):
        list = ["1)", "9)"]
        matches = test_valid_patterns(list, reg.extra_info_pattern)
        self.assertEqual(list, matches)

        # teacher code, one digit too much
        list2 = ["ABBAM", "11)"]
        noMatchesExpectation = [None, None]
        noMatches = test_invalid_patterns(list2, reg.extra_info_pattern)
        self.assertEqual(noMatchesExpectation, noMatches)

    def test_lecture1(self):
        list = ["INFANL02-3", "TINPRJ0178", "CCOCKE10R3", "INFLAB01"]
        matches = test_valid_patterns(list, reg.lecture_pattern1)
        self.assertEqual(list, matches)

        # teacher, class
        list2 = ["ABBAM", "MINBOD02"]
        noMatchesExpectation = [None, None]
        noMatches = test_invalid_patterns(list2, reg.lecture_pattern1)
        self.assertEqual(noMatchesExpectation, noMatches)


    def test_lecture2(self):
        list = ["CMD-DC01-3"]
        matches = test_valid_patterns(list, reg.lecture_pattern2)
        self.assertEqual(list, matches)
        # teacher, class
        list2 = ["ABBAM", "MINBOD02"]
        noMatchesExpectation = [None, None]
        noMatches = test_invalid_patterns(list2, reg.lecture_pattern2)
        self.assertEqual(noMatchesExpectation, noMatches)

    def test_lecture_specific(self):
        list = ["HP-voorlichting"]
        matches = test_valid_patterns(list, reg.lecture_specific)
        self.assertEqual(list, matches)

        # teacher, class
        list2 = ["ABBAM", "MINBOD02"]
        noMatchesExpectation = [None, None]
        noMatches = test_invalid_patterns(list2, reg.lecture_specific)
        self.assertEqual(noMatchesExpectation, noMatches)

    def test_location(self):
        list = ["WD.01.003", "H.5.314"]
        matches = test_valid_patterns(list, reg.location_pattern)
        self.assertEqual(list, matches)

        special = ["H.5.314, H"]
        specialExpected = ["H.5.314"]
        specialMatch = test_valid_patterns(special, reg.location_pattern)
        self.assertEqual(specialExpected, specialMatch)

        # too short, not a location but a class
        list2 = ["WD.1.1", "INF2D"]
        noMatchesExpectation = [None, None]
        noMatches = test_invalid_patterns(list2, reg.location_pattern)
        self.assertEqual(noMatchesExpectation, noMatches)


    def test_lecture_number(self):
        list = ["1", "1800", "2368"]
        matches = test_valid_patterns(list, reg.lecture_number_pattern)
        self.assertEqual(list, matches)

        # not a lecture number but a class
        list2 = ["INF2D"]
        noMatchesExpectation = [None]
        noMatches = test_invalid_patterns(list2, reg.lecture_number_pattern)
        self.assertEqual(noMatchesExpectation, noMatches)

    def test_class1(self):
        list = ["COD2", "COV1D", "INF2D", "DCMD1A", "DINF1", "CMD1A", "TI1A"]
        matches = test_valid_patterns(list, reg.class_pattern1)
        self.assertEqual(list, matches)

        # too short, starts with a number instead of a letter
        list2 = ["C2", "2NF2D"]
        noMatchesExpectation = [None, None]
        noMatches = test_invalid_patterns(list2, reg.class_pattern1)
        self.assertEqual(noMatchesExpectation, noMatches)

    def test_class2(self):
        list = ["BO-COM", "BO-TI", "CMD-BO", "COD-AD3", "CMD-DT01-6", "CMT-BO", "COV3-HP"]
        matches = test_valid_patterns(list, reg.class_pattern2)
        self.assertEqual(list, matches)

        # too short, starts with a number instead of a letter
        list2 = ["B-COM", "2B-COM"]
        noMatchesExpectation = [None, None]
        noMatches = test_invalid_patterns(list2, reg.class_pattern2)
        self.assertEqual(noMatchesExpectation, noMatches)

    def test_class3(self):
        list = ["MINBOD02A", "MINBOD02", "MINIED1C", "MIN ENS02", "MIN IED1B", "MIN SMO", "KEU AAR01", "KEU SOU01K"]
        matches = test_valid_patterns(list, reg.class_pattern3)
        self.assertEqual(list, matches)
        # too short, starts with a number instead of a letter
        list2 = ["MINBD02", "2INBOD02A"]
        noMatchesExpectation = [None, None]
        noMatches = test_invalid_patterns(list2, reg.class_pattern3)
        self.assertEqual(noMatchesExpectation, noMatches)


    def test_class_cmd_lab(self):
        list = ["CMDLABEXP", "CMDLABPT"]
        matches = test_valid_patterns(list, reg.class_cmd_lab_pattern)
        self.assertEqual(list, matches)

        # too short, doesnt start with cmd
        list2 = ["CMDLABQ", "2MDLABEXP"]
        noMatchesExpectation = [None, None]
        noMatches = test_invalid_patterns(list2, reg.class_cmd_lab_pattern)
        self.assertEqual(noMatchesExpectation, noMatches)


    def test_class_specific(self):
        list = ["cmd", "marjo", "opbouw", "overloop", "RESCMD", "TENT", "uitloop lokaal"]
        matches = test_valid_patterns(list, reg.class_specific_pattern)
        self.assertEqual(list, matches)
        # not in the list
        list2 = ["AMIGA"]
        noMatchesExpectation = [None]
        noMatches = test_invalid_patterns(list2, reg.class_specific_pattern)
        self.assertEqual(noMatchesExpectation, noMatches)