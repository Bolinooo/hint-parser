from .url import *
import requests

def start():

    # links_room = build_set("ROOM")
    links_teacher = build_set("TEACHER")
    for link in sorted(links_teacher):
        print(link)


