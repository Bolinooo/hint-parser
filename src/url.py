from .decorator import *
from .helper import *
import requests


@validate_response
def get_response(url):
    """
    Function to return response code
    :param url: url to be checked
    :return: result of validate_response
    """
    return url


def build_sequence(n):
    """
    Function to build sequence of strings for url
    :param n: Number of strings to convert
    :return: set of strings
    """
    seq = set()
    for i in range(1, n + 1):
        seq.add(apply_format(i))
    return seq