import configparser
import os

def fun(x):
    return x + 1


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


