from multiprocessing.dummy import Pool as ThreadPool
from .parser import *
from .url import *


import time
import argparse


def main():
    """
    Main flow of the parser
    1) Gather command line arguments
    2) Crawl all available links
    3) Parse all the valid responses
    4) Store length of list for each option
    5) Convert them to dict
    6) Parse final dict to a json/csv
    """

    filename = "config.ini"
    cfg = get_config(filename)

    global settings
    settings = []

    settings




    parser = argparse.ArgumentParser()
    parser.add_argument("option", type=str, help="Value for option to parser")
    parser.add_argument("quarter", type=int, help="Value for quarter to parser")
    args = parser.parse_args()
    option = args.option
    quarter = args.quarter

    cfg.remove_section('OPTIONS')
    cfg.remove_section('QUARTER')

    cfg.add_section('OPTIONS')
    cfg.add_section('QUARTER')

    cfg.set('OPTIONS', option, option[0])
    cfg.set('QUARTER', "NUMBER", str(quarter))

    with open(os.path.join(os.path.dirname(__file__), filename), 'w') as configfile:
        cfg.write(configfile)




    start_time = time.time()

    # Step 1) Crawl all available links
    threads = ThreadPool(2)
    data = threads.map(build_responses, cfg.options('OPTIONS'))

    parsed_items = []
    parsed_counters = {}

    for dd in data: # dd = defaultdict
        # Step 2) Parse all the responses
        for option, responselist in dd[0].items():
            parsed_counters[option] = len(responselist)
            parsed_items.append([parse(resp[0]) for resp in responselist])
            print("Succesfully parsed all responses for {option}".format(option=option))
        # Step 3) Store length of list for each option
        for option, timedata in dd[1].items():
            if len(timedata) == parsed_counters[option]:
                parsed_counters[option] = (len(timedata), timedata)
                print("Succesfully stored additional data [quarter, week] for {option}".format(option=option))

    # Step 4) Convert them to dict
    final = compare_dicts(parsed_items, parsed_counters)

    # Step 5) Parse final dict to a json
    options = [
        'abbrevation',
        'floor',
        'room'
    ]
    convert_csv(final, options, skip_empty=True, unique=True)

    print("Parser is finished. It took {seconds} seconds.".format(seconds=round(time.time() - start_time)))
    configfile.close()
    # teacher = 3504
    # classes = 2534
    # rooms = 986
