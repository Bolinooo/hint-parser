from .decorator import *
from .helper import *
import requests

cfg = get_config('config.ini')

@validate_response
def get_response(url):
    """
    Function to return response code
    :param url: url to be checked
    :return: result of validate_response
    """
    return url

