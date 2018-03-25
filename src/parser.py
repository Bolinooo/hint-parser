from .url import *
import requests


def start():

    # links_room = build_set("ROOM")
    links = build_dict()
    for link in sorted(links):
        print(link)


