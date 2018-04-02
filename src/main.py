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
    pool = ThreadPool(4)
    links = pool.map(build_urls, cfg.options('OPTIONS'))

    parsed_items = []
    parsed_counters = {}

    for dd in links: # dd = defaultdict
        # Step 2) Parse all the valid responses
        for k, v in dd[0].items():
            parsed_counters[k] = len(v)
            parsed_items.append([parse(resp[0]) for resp in v])
        # Step 3) Store length of list for each option
        for k, v in dd[1].items():
            if len(v) == parsed_counters[k]:
                parsed_counters[k] = (len(v), v)

    # Step 4) Convert them to dict
    final = compare_dicts(parsed_items, parsed_counters)

    # Step 5) Parse final dict to a json
    convert_dict(final)
    print("Parser is finished. It took {seconds}".format(seconds=time.time() - start_time))
    # teacher = 3504
    # classes = 2534
    # rooms = 986
