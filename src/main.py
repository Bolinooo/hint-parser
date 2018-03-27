from .parser import *


def main():

    links = build_dict()
    extracted_links = [[i for i in links[key]] for key in links.keys()]

    for list in links.values():
        with open("output.txt", "w") as text_file:
           text_file.write(list)
