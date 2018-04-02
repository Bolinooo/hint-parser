import configparser
import os
import json


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


def convert_dict(dictionary):
    """
    Function to convert dictionary to a json file using built-in module
    :param dictionary: Dictionary with all results
    :return: .json-file
    """
    assert type(dictionary) is dict
    return json.dumps(dictionary, sort_keys=True)
