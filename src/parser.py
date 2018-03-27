from .url import *
import configparser

def start():

    links = build_dict()
    extracted_links = [[i for i in links[key]] for key in links.keys()]

    x = 0
    for item in links.values():
        print(item)