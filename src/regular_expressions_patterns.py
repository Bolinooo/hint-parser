teacher_pattern = r"[A-Z]{5}$"
lecture_pattern = r"[A-Z]{6}[\d]{2}"
hp_pattern = r"HP-voorlichting"
room_pattern = r"[A-Z]{1,2}\.[\d]{1,2}\.[\d]{3}"
extra_info_pattern = r"[\d]\)"
lecture_number_pattern = r"[\d]{1,4}$"
# class has even more types
class_pattern = r"[\w]{5}$"

# 2 ltr with a -
# BO-COM, BO-TI
class_2 = r"[A-Z]{2}-"
# 3 ltr with a -
# CMD-BO, COD-AD3
class_3 = r"[A-Z]{3}-"
# 3 ltr, 1 nr
# COD2
class_4 = r"[A-Z]{3}[\d]{1}"
# this one is empty so maybe this is not needed
# COV3-HP
class_5 = r"[A-Z]{3}[\d]{1}-"
# 4 letters, 1 nr, 1 letter
# DCMD1A
class_6 = r"[A-Z]{4}[\d]{1}[A-Z]{1}$"
class_cmd = r"cmd"
class_marjo = r"marjo"
class_opbouw = r"opbouw"
class_overloop = r"overloop"
class_rescmd= r"RESCMD"
class_tent = r"TENT"
class_uitloop_lokaal= r"uitloop lokaal"
# 4 ltr, 1 digit
# DINF1
class_7 = r"[A-Z]{4}[\d]{1}$"
#
# KEU AAR01, KEU SOU01K
class_8 = r""
# MIN ENS02, MIN IED1B, MIN SMO
class_9 = r""
# MINBOD02A, MINBOD02
class_10 = r""
# MINIED1C
class_11 = r""
# TI1A
class_12 = r""
# CMD-DT01-6
class_13 = r""
# CMDLABEXP, CMDLABPT
class_14 = r""
# CMT-BO
class_15 = r""
# 3 letters, 1 number, 1 letter
# CMD1A, COV1D
class_1 = r"[A-Z]{3}[\d]{1}[A-Z]{1}$"


