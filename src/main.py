from .parser import *
from .url import *

import time
import argparse


def main():
    """
    Main flow of the parser
    1) Gather command line arguments
    2) Set global settings
    3) Crawl all available links
    4) Parse all the valid responses
    5) Store length of list for each option
    6) Convert them to dict
    7) Parse final dict to a json/csv
    """

    start_time = time.time()

    # 1 Gather command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("option", type=str, help="Value for option to parser")
    parser.add_argument("quarter", type=int, help="Value for quarter to parser")
    args = parser.parse_args()
    option = args.option
    quarter = args.quarter

    # 2 Set global settings
    settings = {
        'teacher': 't',
        'schedule': 'c',
        'classes': 'c',
        'rooms': 'r',
        'base_url': "http://misc.hro.nl/roosterdienst/webroosters/",
        'teacher_items': ['title_blue', 'title_black'],
        'rooms_items': ['title_blue', 'title_black'],
        'classes_items': ['title_blue', 'title_black'],
        'schedule_items': ['date_full', 'start_time', 'end_time', 'subject', 'teacher', 'building', 'floor', 'room', 'abbrevation', 'title', 'lecture', 'lecture_nr', 'extra_info']
    }
    mylist = [settings[option]]

    # 3 Crawl all available links
    data = [build_responses(option, quarter, settings) for x in mylist]

    parsed_items = []
    parsed_sidedata = {}
    for dd in data:
        # 4 Parse all the responses
        for option, responselist in dd[0].items():
            parsed_sidedata[option] = len(responselist)
            parsed_items.append([parse(resp[0], option) for resp in responselist])
            print("Succesfully parsed all responses for {option}".format(option=option))
        # 5 Store length of list for each option
        for option, timedata in dd[1].items():
            if len(timedata) == parsed_sidedata[option]:
                parsed_sidedata[option] = (len(timedata), timedata)
                print("Succesfully stored additional data [quarter, week] for {option}".format(option=option))

    # 6 Convert them to dict
    final = combine_dicts(parsed_items, parsed_sidedata)

    # 7 Parse final dict to a csv
    convert_csv(
        dictionary=final,
        option=option,
        quarter=quarter,
        settings=settings,
        skip_empty=True,
        unique=True)

    print("Parser is finished. It took {seconds} seconds.".format(seconds=round(time.time() - start_time)))
