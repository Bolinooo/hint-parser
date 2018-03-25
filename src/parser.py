from .url import *
import requests


def start():

    links = build_dict()
    extracted_links = [[i for i in links[key]] for key in links.keys()]
