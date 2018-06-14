import json
import csv
import time
import calendar
import os
import sys

def apply_format(n):
    """
    Function to convert number to string in 6-digit format
    :param n: number to convert
    :return: string format
    """
    return format(n, "05")


def build_filename(option, quarter):
    """
    Function to build filename based on current day and month
    :return: Name of the file. Example: 'teacher_q1_timestamp'
    """
    timestamp = calendar.timegm(time.gmtime())
    underscore = "_"
    name = [option, underscore, "q" + str(quarter), underscore, str(timestamp)]
    return "".join(name)


def convert_json(dictionary, option, quarter):
    """
    Function to convert dictionary to a json file using built-in module
    :param dictionary: Dictionary with all results
    :param option: Option from command line
    :param quarter: Quarter from command line
    :return: .json-file in root dir
    """
    assert type(dictionary) is dict
    filename = build_filename(option, quarter)
    with open('%s.json' % filename, 'w') as file:
        file.write(json.dumps(dictionary, indent=4, sort_keys=True))
    file.close()


def strip_csv(csvfile, option, quarter):
    """
    Function to strip csv records to a new csv with unique values
    :param csvfile: Initial csv file
    :param option: Option from command line
    :param quarter: Quarter from command line
    :return: New csv file with unique values
    """
    filename = build_filename(option, quarter)
    with open(csvfile.name, 'r') as in_file, open(os.path.dirname(sys.modules['__main__'].__file__) + "/output/%s_unique.csv" % filename, 'w') as out_file:
        seen = set()
        for line in in_file:
            seen.add(line)

        for line in sorted(seen):
            out_file.write(line)


def convert_csv(**kwargs):
    """
    Function to convert final dictionary to a json file using built-in module
    :return: .csv-file in root dir
    """
    dictionary = kwargs['dictionary']
    option = kwargs['option']
    quarter = kwargs['quarter']
    settings = kwargs['settings']
    skip_empty = kwargs['skip_empty']
    unique = kwargs['unique']

    assert type(dictionary) is dict
    filename = build_filename(option, quarter)
    with open(os.path.dirname(sys.modules['__main__'].__file__) + "/output/%s.csv" % filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for k1, v1 in dictionary.items(): # option
            for k2, v2 in v1.items(): # quarter
                for k3, v3 in v2.items(): # week
                    for item in v3:
                        for cell in item:
                            row = extract_item(cell, settings, option, skip_empty)
                            if row:
                                writer.writerow(row)

    if unique:
        strip_csv(csvfile, option, quarter)

    csvfile.close()


def extract_item(parsed_dict, settings, option, skip_empty=False):
    """
    Function to parse a dictionary item into a single row
    :param parsed_dict: Parsed dictionary
    :param settings: List of individual options to get from each schedule item
    :param option: Option from command line
    :param skip_empty: Boolean to set of rows with empty values should be skipped
    :return: Iterable with items that should be in row
    """

    if option != "schedule":
        possibilities = {
            'title_blue': parsed_dict.get("title_blue", "No abbrevation"),
            'title_black': parsed_dict.get("title_black", "No item")
        }
    else:
        possibilities = {
            'abbrevation': parsed_dict.get("abbrevation", "empty"),
            'title': parsed_dict.get("title", "empty"),
            'lecture_nr': parsed_dict["info"].get("lecture_nr", "empty"),
            'extra_info': parsed_dict["info"].get("extra_info", "empty"),
            'subject': parsed_dict["info"].get("event", "empty"),
            'date_full': parsed_dict.get("date_full", "empty"),
            'date_year': parsed_dict.get("date_year", "empty"),
            'date_month': parsed_dict.get("date_month", "empty"),
            'date_day': parsed_dict.get("date_day", "empty"),
            'start_time': parsed_dict.get("start_begin", "empty"),
            'end_time': parsed_dict.get("end_end", "empty"),
            'start_block': parsed_dict.get("start_block", "empty"),
            'end_block': parsed_dict.get("end_block", "empty"),
            'building': parsed_dict["info"].get("building", "empty"),
            'floor': parsed_dict["info"].get("floor", "empty"),
            'room': parsed_dict["info"].get("room", "empty"),
            'teacher': parsed_dict["info"].get("teacher", "empty"),
            'lecture': parsed_dict["info"].get("lecture", "Not available"),
            'allday': str(True) if parsed_dict.get("start_block") is 1 and parsed_dict.get("end_block") is 15 else str(False)
        }
    final = []

    for key in settings[option + "_items"]:
        if key in possibilities:
            if skip_empty and possibilities[key] is "empty":
                break
            final.append(possibilities[key])

    return final
