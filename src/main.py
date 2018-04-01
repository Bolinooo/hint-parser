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
    """

    start_time = time.time()

    # Step 1) Crawl all available links
    pool = ThreadPool(4)
    links = pool.map(build_urls, cfg.options('OPTIONS'))

    # Step 2) Parse all the valid responses
    parsed_items = []
    for dd in links:
        for k, v in dd[0].items():
            parsed_items.append([parse(resp[0]) for resp in v])

    # Step 3) Store length of list for each option
    counters = {}
    for dd in links:
        for k, v in dd[1].items():
            counters[k] = (len(v), v)

    # Step 4) TODO = Convert them to dict (work in progress)
    # convert_dicts(parsed_items, data)

    print("--- %s seconds ---" % (time.time() - start_time))
    # teacher = 3504
    # classes = 2534
    # rooms = 986
