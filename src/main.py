from multiprocessing.dummy import Pool as ThreadPool
from .parser import *
from .url import *
import time


def main():
    """
    Main flow of the parser
    1) Crawl all available links
    2) Parse all the valid responses
    3) Store length of list for each option
    4) Convert them to dict
    5) Parse final dict to a json
    """

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
    convert_csv(final)
    print("Parser is finished. It took {seconds} seconds.".format(seconds=round(time.time() - start_time)))

    # teacher = 3504
    # classes = 2534
    # rooms = 986
