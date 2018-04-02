import configparser
import os
import json
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
    order = ['schedule_', time_format]
    return "".join(order)


def convert_dict(dictionary):
    """
    Function to convert dictionary to a json file using built-in module
    :param dictionary: Dictionary with all results
    :return: .json-file
    """
    assert type(dictionary) is dict
    filename = build_filename()
    with open('%s.json' % filename, 'w') as file:
        file.write(json.dumps(dictionary, sort_keys=True))
    file.close()
