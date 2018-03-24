from .decorator import *
from .helper import *


cfg = get_config('config.ini')

@validate_response
def get_response(url):
    """
    Function to return response code
    :param url: url to be checked
    :return: result of validate_response
    """
    return url


def build_set(option):
    """
    Function to build set of links with status code 200 for defined option
    :param option: Option from config-file: TEACHER, ROOM or COURSE
    :return: set of links with given option
    """

    base = cfg["URL"]["BASE"]
    quarter = cfg["SETTINGS"]["QUARTER"]
    education = cfg["SETTINGS"]["EDUCATION"]
    option = cfg["OPTIONS"][option]

    base_url = base + education + "/kw" + quarter + "/"
    links = set()
    connected = True

    for week in range(13, 20, 1):
        num = 1
        while connected:
            url = base_url + str(week) + "/" + option + "/" + option + apply_format(num) + ".htm"
            resp = get_response("{0}".format(url))
            if resp[1] != 200:
                connected = False
            else:
                links.add(url)
            num += 1
    return links
