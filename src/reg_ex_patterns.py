import re
# list = ["ABBAM", "AMIGA", "MINUA"]
teacher_pattern = r"[A-Z]{5}$"
# list = ["1)", "9)"]
extra_info_pattern = r"\d\)"
# list = ["INFPRJ00-3", "TINPRJ0178","CCOCKE10R3","HP-voorlichting", "INFLAB01", "CMD-DC01-3"]
lecture_pattern = r"[A-Z]{6}\d{2,4}(-\d)?([A-Z]\d)?|HP-voorlichting|[A-Z]{3}-[A-Z]{2}\d{2}-\d"
# list = ["WD.01.003", "H.5.314"]
location_pattern = r"[A-Z]{1,2}\.\d{1,2}\.\d{3}"
# list = ["1", "1800", "2368"]
lecture_number_pattern = r"\d{1,4}$"

# list = ["COD2", "COV1D", "INF2D","DCMD1A", "DINF1", "CMD1A", "TI1A"]
# 2-4 letters, 1 digit, maybe 1 letter
class1_pattern = r"[A-Z]{2,4}\d{1}[A-Z]{0,1}$"
# list = ["BO-COM", "BO-TI", "CMD-BO","COD-AD3", "CMD-DT01-6", "CMT-BO", "COV3-HP"]
# 2-3 letters, maybe 1 letter, 1 dash, 2-4 alphanum, maybe 1 dash,
class2_pattern = r"[A-Z]{2,3}\d?-\w{2,4}-?\d?"
# list = ["MINBOD02A", "MINBOD02","MINBOD02-3", "MINIED1C", "MIN ENS02", "MIN IED1B", "MIN SMO", "KEU AAR01", "KEU SOU01K"]
class3_pattern = r"[A-Z]{3} ?[A-Z]{3}(\d{1,2})?[A-Z]?(-\d)?"
# list = ["CMDLABEXP", "CMDLABPT"]
class_cmd_lab_pattern = r"CMDLAB[A-Z]{2,3}"
# specific patterns
# list = ["cmd","marjo","opbouw","overloop", "RESCMD", "TENT","uitloop lokaal"]
class_specific_pattern = r"cmd|marjo|opbouw|overloop|RESCMD|TENT|uitloop lokaal"

reg_ex_dict = {}
reg_ex_dict["teacher"] = [teacher_pattern]
reg_ex_dict["extra_info"] = [extra_info_pattern]
reg_ex_dict["location"] = [location_pattern]
reg_ex_dict["lecture"] = [lecture_pattern]
reg_ex_dict["lecture_nr"] = [lecture_number_pattern]
reg_ex_dict["class"] = [class1_pattern, class2_pattern, class3_pattern, class_cmd_lab_pattern, class_specific_pattern]