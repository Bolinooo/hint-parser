from src import reg_ex_patterns as file

import unittest
import  re

def test_helper(list, pattern):
    newList = []
    for item in list:
        matched = re.match(pattern, item)
        if(matched == None):
            raise ValueError(item + ' does not match the pattern')
        newList.append(matched.group())
    return  newList

class MyRegExTest(unittest.TestCase):
    def test_teacher(self):
        list = ["ABBAM", "AMIGA", "MINUA"]
        matches = test_helper(list, file.teacher_pattern)
        self.assertEqual(list, matches)

    def test_extra_info(self):
        list = ["1)", "9)"]
        matches = test_helper(list, file.extra_info_pattern)
        self.assertEqual(list, matches)

    def test_lecture(self):
        list = ["INFPRJ00-3", "TINPRJ0178","CCOCKE10R3","HP-voorlichting", "INFLAB01", "CMD-DC01-3"]
        matches = test_helper(list, file.lecture_pattern)
        self.assertEqual(list, matches)

    def test_location(self):
        list = ["WD.01.003", "H.5.314"]
        matches = test_helper(list, file.location_pattern)
        self.assertEqual(list, matches)

        special = "H.5.314, H"
        m = re.match(file.location_pattern, special)
        self.assertEqual(m.group(), "H.5.314")

    def test_lecture_number(self):
        list = ["1", "1800", "2368"]
        matches = test_helper(list, file.lecture_number_pattern)
        self.assertEqual(list, matches)

    def test_class1(self):
        list = ["COD2", "COV1D", "INF2D", "DCMD1A", "DINF1", "CMD1A", "TI1A"]
        matches = test_helper(list, file.class1_pattern)
        self.assertEqual(list, matches)

    def test_class2(self):
        list = ["BO-COM", "BO-TI", "CMD-BO", "COD-AD3", "CMD-DT01-6", "CMT-BO", "COV3-HP"]
        matches = test_helper(list, file.class2_pattern)
        self.assertEqual(list, matches)

    def test_class3(self):
        list = ["MINBOD02A", "MINBOD02","MINBOD02-3", "MINIED1C", "MIN ENS02", "MIN IED1B", "MIN SMO", "KEU AAR01", "KEU SOU01K"]
        matches = test_helper(list, file.class3_pattern)
        self.assertEqual(list, matches)

    def test_class_cmd_lab(self):
        list = ["CMDLABEXP", "CMDLABPT"]
        matches = test_helper(list, file.class_cmd_lab_pattern)
        self.assertEqual(list, matches)

    def test_class_specific(self):
        list = ["cmd", "marjo", "opbouw", "overloop", "RESCMD", "TENT", "uitloop lokaal"]
        matches = test_helper(list, file.class_specific_pattern)
        self.assertEqual(list, matches)