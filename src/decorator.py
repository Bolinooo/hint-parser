import functools
import requests


def validate_response(func):
    """
    Decorator to check availability url
    :param func: get_response(url)-function
    :return: If valid a 200 statuscode, if invalid None
    """
    @functools.wraps(func)
    def newfunc(url):
        try:
            response = requests.get(url)
            return response.status_code
        except Exception as e:
            return None
    return newfunc
