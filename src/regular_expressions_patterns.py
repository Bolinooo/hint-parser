teacher_pattern = r"[A-Z]{5}$"
# list = ["INFPRJ00-3", "TINPRJ0178","CCOCKE10R3","HP-voorlichting", "INFLAB01", "CMD-DC01-3"]
lecture_pattern = r"[A-Z]{6}\d{2,4}(-\d)?([A-Z]\d)?|HP-voorlichting|[A-Z]{3}-[A-Z]{2}\d{2}-\d"
# list = ["WD.01.003", "H.5.314"]
location_pattern = r"[A-Z]{1,2}\.\d{1,2}\.\d{3}"

extra_info_pattern = r"\d\)"
lecture_number_pattern = r"\d{1,4}$"
# class has even more types
class_pattern = r"\w{5}$"
# list = ["COD2", "COV1D", "INF2D","DCMD1A", "DINF1", "CMD1A", "TI1A"]
class_pattern1 = r"[A-Z]{2,4}\d{1}[A-Z]{0,1}$"
# list = ["BO-COM", "BO-TI", "CMD-BO","COD-AD3", "CMD-DT01-6", "CMT-BO", "COV3-HP"]
class_pattern2 = r"[A-Z]{2,3}\d?-\w{2,4}-?\d?"
# CMDLABEXP, CMDLABPT
class_cmd_lab = r"CMDLAB[A-Z]{1,2}"
# specific patterns
class_specific = r"cmd | marjo | opbouw | overloop| RESCMD| TENT | uitloop lokaal"

#
# KEU AAR01, KEU SOU01K
class_8 = r""
# MIN ENS02, MIN IED1B, MIN SMO
class_9 = r""
# MINBOD02A, MINBOD02
class_10 = r""
# MINIED1C
class_11 = r""
