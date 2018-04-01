from multiprocessing.dummy import Pool as ThreadPool
from .parser import *
from .url import *
import time


def main():
    """
    Main flow of the parser
    1) Crawl all available links
    2) Parse all the valid responses
    3) ...
    """

    start_time = time.time()

    # Crawl all available links using threads
    pool = ThreadPool(4)
    links = pool.map(build_urls, cfg.options('OPTIONS'))

    # Map the parse()-function over each response from each option
    parsed_items = []
    counters = {}

    for dd in links:
        for k, v in dd[0].items():
            parsed_items.append([parse(resp[0]) for resp in v])

    for dd in links:
        for k, v in dd[1].items():
            counters[k] = len(v)


    # convert_dicts(parsed_items, data)

    print("--- %s seconds ---" % (time.time() - start_time))
    # teacher = 3504
    # classes = 2534
    # rooms = 986
