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
    # Crawl all available links
    pool = ThreadPool(4)
    links = pool.map(build_urls, cfg.options('OPTIONS'))

    urls, data = links[0][0], links[0][1]

    # Map the parse()-function over each response in each option
    parse_list = []
    for option, list in urls.items():
        parse_list += [parse(response) for response in list]


    print("--- %s seconds ---" % (time.time() - start_time))
    # teacher = 3504
    # classes = 2534
    # rooms = 986
