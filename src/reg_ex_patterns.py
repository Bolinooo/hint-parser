import re
# list = ["ABBAM", "AMIGA", "MINUA"]
# match exactly 5 letters
teacher_pattern = r"[A-Z]{5}$"

# list = ["1)", "9)"]
# 1 digit, 1 parentheses
extra_info_pattern = r"[0-9]\)"

# list = ["INFPRJ00-3", "TINPRJ0178","CCOCKE10R3", "INFLAB01"]
# 6 letters, 2-4 digits, maybe(1 dash, digit) or maybe(1 letter, 1 digit)
lecture_pattern1 = r"[A-Z]{6}[0-9]{2,4}((-[0-9])|([A-Z][0-9]))?"
# list = ["CMD-DC01-3"]
# 3 letters, 1 dash, 2 letters, 2 digits, 1 dash, 1 digit
lecture_pattern2 = r"[A-Z]{3}-[A-Z]{2}[0-9]{2}-[0-9]"
# list = ["HP-voorlichting"]
# specific lectures
lecture_specific = r"HP-voorlichting"

# list = ["WD.01.003", "H.5.314"]
# 1-2 letters, 1 dot, 1-2 digit(s), 1 dot, 3 digits
location_pattern = r"[A-Z]{1,2}\.[0-9]{1,2}\.[0-9]{3}"

# list = ["1", "1800", "2368"]
# 1-4 digits
lecture_number_pattern = r"[0-9]{1,4}$"

# list = ["COD2", "COV1D", "INF2D","DCMD1A", "DINF1", "CMD1A", "TI1A"]
# 2-4 letters, 1 digit, maybe 1 letter
class_pattern1 = r"[A-Z]{2,4}[0-9]{1}[A-Z]{0,1}$"
# list = ["BO-COM", "BO-TI", "CMD-BO","COD-AD3", "CMD-DT01-6", "CMT-BO", "COV3-HP"]
# 2-3 letters, maybe 1 letter, 1 dash, 2-4 alphanum, maybe 1 dash,
class_pattern2 = r"[A-Z]{2,3}[0-9]?-\w{2,4}-?[0-9]?"
# list = ["MINBOD02A", "MINBOD02", "MINIED1C", "MIN ENS02", "MIN IED1B", "MIN SMO", "KEU AAR01", "KEU SOU01K"]
# 3 letters, maybe 1 space, 3 letters,  maybe (1-2 digits, maybe 1 letter)
class_pattern3 = r"[A-Z]{3} ?[A-Z]{3}([0-9]{1,2}[A-Z]?)?"
# list = ["CMDLABEXP", "CMDLABPT"]
# starts with CMDLAB, 2-3 letters
class_cmd_lab_pattern = r"CMDLAB[A-Z]{2,3}"
# specific patterns
# list = ["cmd","marjo","opbouw","overloop", "RESCMD", "TENT","uitloop lokaal"]
class_specific_pattern = r"cmd|marjo|opbouw|overloop|RESCMD|TENT|uitloop lokaal"

reg_ex_dict = {}
reg_ex_dict["teacher"] = [teacher_pattern]
reg_ex_dict["extra_info"] = [extra_info_pattern]
reg_ex_dict["location"] = [location_pattern]
reg_ex_dict["lecture"] = [lecture_pattern1, lecture_pattern2, lecture_specific]
reg_ex_dict["lecture_nr"] = [lecture_number_pattern]
reg_ex_dict["class"] = [class_pattern1, class_pattern2, class_pattern3, class_cmd_lab_pattern, class_specific_pattern]