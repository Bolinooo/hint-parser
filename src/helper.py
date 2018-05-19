import configparser
import os
import json
import csv
import datetime


def get_config(filename):
    """
    Function to obtain the config.ini-file
    :param filename: Name of the config.ini-file
    :return: configparser.Configparser-object
    """
    config = configparser.ConfigParser()
    path = os.path.join(os.path.dirname(__file__), filename)
    config.read(path)

    if not os.path.isfile(path):
        return None
    return config


def apply_format(n):
    """
    Function to convert number to string in 6-digit format
    :param n: number to convert
    :return: string format
    """
    return format(n, "05")


def build_filename():
    """
    Function to build filename based on current day and month
    :return: 'schedule_day_month'-string
    """
    current = datetime.datetime.now()
    time_format = current.strftime('%d-%m')
    name = ['schedule_', time_format]
    return "".join(name)


def convert_json(dictionary):
    """
    Function to convert dictionary to a json file using built-in module
    :param dictionary: Dictionary with all results
    :return: .json-file in root dir
    """
    assert type(dictionary) is dict
    filename = build_filename()
    with open('%s.json' % filename, 'w') as file:
        file.write(json.dumps(dictionary, indent=4, sort_keys=True))
    file.close()


def strip_csv(csvfile):
    """
    Function to strip csv records to a new csv with unique values
    :param csvfile: Initial csv file
    :return: New csv file with unique values
    """
    filename = build_filename()
    with open(csvfile.name, 'r') as in_file, open('%s_unique.csv' % filename,'w') as out_file:
        seen = set()
        for line in in_file:
            seen.add(line)

        for line in sorted(seen):
            out_file.write(line)


def convert_csv(dictionary, items, skip_empty=False, unique=False):
    """
    Function to convert final dictionary to a json file using built-in module
    :param dictionary: Dictionary with all results
    :param items: List of individual options to get from each schedule item
    :param skip_empty: Boolean to set of rows with empty values should be skipped
    :param unique: Boolean to set of all values should be unique
    :return: .csv-file in root dir
    """
    assert type(dictionary) is dict
    filename = build_filename()
    with open('%s.csv' % filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for k1, v1 in dictionary.items(): # option
            for k2, v2 in v1.items(): # quarter
                for k3, v3 in v2.items(): # week
                    for item in v3:
                        for cell in item:
                            row = extract_item(cell, items, skip_empty)
                            if row:
                                writer.writerow(row)

    if unique:
        strip_csv(csvfile)

    csvfile.close()


def extract_item(parsed_dict, items, skip_empty=False):
    """
    Function to parse a dictionary item into a single row
    :param parsed_dict: Parsed dictionary
    :param items: List of individual options to get from each schedule item
    :param skip_empty: Boolean to set of rows with empty values should be skipped
    :return: Iterable with items that should be in row
    """
    possibilities = {
        'subject': parsed_dict["info"].get("event", parsed_dict["info"].get("lecture", "Not available")),
        'start_date': parsed_dict.get("date", "empty"),
        'start_time': parsed_dict.get("start_begin", "empty"),
        'end_date': parsed_dict.get("date", "empty"),
        'end_time': parsed_dict.get("end_end", "empty"),
        'start_block': parsed_dict.get("start_block", "empty"),
        'end_block': parsed_dict.get("end_block", "empty"),
        'building': parsed_dict["info"].get("building", "empty"),
        'floor': parsed_dict["info"].get("floor", "empty"),
        'room': parsed_dict["info"].get("room", "empty"),
        'allday': str(True) if parsed_dict.get("start_block") is 1 and parsed_dict.get("end_block") is 15 else str(False)
    }

    final = []
    for key in items:
        if key in possibilities:
            if skip_empty and possibilities[key] is "empty":
                break
            final.append(possibilities[key])

    return final
