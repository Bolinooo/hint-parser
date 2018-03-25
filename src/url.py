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


def build_dict():
    """
    Function to build dict of links with status code 200 for all options in config.ini
    :return: set of links with given option
    """

    links = {}
    connected = True

    for option in cfg.options("OPTIONS"):
        for week in range(1, 52):
            num = 1
            while connected:
                url = build_url(option, week, num)
                resp = get_response("{0}".format(url))
                if resp[1] != 200:
                    break
                else:
                    if option not in links:
                        links.setdefault(option, [])
                    links[option].append(url)
                num += 1
    return links


def build_url(option, week, num):

    base = cfg["URL"]["BASE"]
    quarter = cfg["SETTINGS"]["QUARTER"]
    education = cfg["SETTINGS"]["EDUCATION"]
    option = cfg["OPTIONS"][option]

    base_url = base + education + "/kw" + quarter + "/"

    return base_url + str(week) + "/" + option + "/" + option + apply_format(num) + ".htm"
