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
    Function to build dict of links with status code 200
    :return: dict of links for each option
    """
    links = {}
    connected = True

    for option in cfg.options("OPTIONS"):
        for quarter in range(1, 5):
            for week in range(1, 53):
                print("Checking for {0} in quarter {1} for week {2}".format(option, quarter, week))
                num = 1
                while connected:
                    url = build_url(
                        quarter=quarter,
                        option=option,
                        week=week,
                        num=num
                    )
                    resp = get_response("{0}".format(url))
                    if resp[1] != 200:
                        break
                    else:
                        if option not in links:
                            links.setdefault(option, [])
                        links[option].append(url)
                    num += 1
    print("Succesfully build dicts with all available links in schedule.")
    return links


def build_url(**kwargs):
    """
    Function to build url based on given input
    :param kwargs: dict with following keys: option, quarter, week and num
    :return: constructed url string
    """
    base = cfg["URL"]["BASE"]
    education = cfg["SETTINGS"]["EDUCATION"]
    option = cfg["OPTIONS"][kwargs['option']]

    base_url = base + education + "/kw" + str(kwargs['quarter']) + "/"

    return base_url + str(kwargs['week']) + "/" + option + "/" + option + apply_format(kwargs['num']) + ".htm"
