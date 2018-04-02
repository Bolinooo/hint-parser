from collections import defaultdict
from .helper import *
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
    except Exception as e:
        return None
    return response, response.status_code


def build_urls(option):
    """
    Function to build data structure of responses with statuscode 200 and side information
    :return: Two defaultdicts, (1) containing all responses (2) containing week and quarter
    """
    urls = defaultdict(list)
    data = defaultdict(list)

    for quarter in range(1, 5):
        for week in range(1, 53):
            print("Checking for {o} in quarter {q} for week {w}".format(o=option, q=quarter, w=week))
            num = 1
            while True:
                url = build_url(quarter=quarter, option=option, week=week, num=num)
                resp = get_response("{0}".format(url))
                if resp[1] != 200:
                    break
                else:
                    urls[option].append([resp[0]])
                    data[option].append([quarter,week])
                num += 1
    print("Succesfully build dict for {option}".format(option=option))
    return urls, data


def build_url(**kwargs):
    """
    Function to build url based on given input
    :param kwargs: dict with following keys: option, quarter, week and num
    :return: constructed url string
    """
    base = cfg["URL"]["BASE"]
    education = cfg["SETTINGS"]["EDUCATION"]
    option = cfg["OPTIONS"][kwargs['option']]

    week = str(kwargs['week'])
    base_quarter = '/kw'
    quarter = str(kwargs['quarter'])
    slash = "/"
    num = apply_format(kwargs['num'])
    extension = ".htm"

    url = [base, education, base_quarter, quarter, slash, week, slash, option, slash, option, num, extension]

    return "".join(url)
