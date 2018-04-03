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


def convert_csv(dictionary):
    """
    Function to convert final dictionary to a json file using built-in module
    :param dictionary: Dictionary with all results
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
                            row = extract_item(cell)
                            print(",".join(row))
                            writer.writerow(row)
    csvfile.close()


def extract_item(parsed_dict):
    """
    Function to parse a dictionary item into a single row
    :param parsed_dict: Parsed dictionary
    :return: Iterable with items that should be in row
    """
    print(parsed_dict)
    subject = parsed_dict["info"].get("event",
              parsed_dict["info"].get("lecture", "reservering"))
    start_date = parsed_dict.get("date", "not available")
    start_time = parsed_dict.get("start_begin", "not available")
    end_date = parsed_dict.get("date", "not available")
    end_time = parsed_dict.get("end_end", "not available")
    start_block = parsed_dict.get("start_block", "not available")
    end_block = parsed_dict.get("end_block", "not available")
    location = parsed_dict["info"].get("room", "No room found")

    allday = False
    if start_block is 1 and end_block is 15:
        allday = True

    final = [
        subject,
        start_date,
        start_time,
        end_date,
        end_time,
        str(allday),
        "-",
        location
    ]
    return final
