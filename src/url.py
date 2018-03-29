from .helper import *
from collections import defaultdict
import requests


cfg = get_config('config.ini')


def get_response(url):
    """
    Function to return response code
    :param url: url to be checked
    :return: result of validate_response
    """
    try:
        response = requests.get(url)
        return response, response.status_code
    except Exception as e:
        return None


def build_dict(option):
    """
    Function to build dict of links with statuscode 200
    :return: dict of links for each option
    """

    links = defaultdict(list)

    for quarter in range(1, 2):
        for week in range(1, 53):
            print("Checking for {0} in quarter {1} for week {2}".format(option, quarter, week))
            num = 1
            while True:
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
                    links[option].append([resp[0], quarter, option, week])
                num += 1
    print("Succesfully build dict for {option}".format(option=option))
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
    week = str(kwargs['week'])
    slash = "/"
    num = apply_format(kwargs['num'])
    extension = ".htm"

    url = [base_url, week, slash, option, slash, option, num, extension]

    return "".join(url)
