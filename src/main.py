from multiprocessing.dummy import Pool as ThreadPool
from .parser import *
from .url import *


def main():
    """
    Main flow of the parser
    1) Crawl all available links
    2) Parse all the valid responses
    3) ...
    """

    # Crawl all available links
    pool = ThreadPool(4)
    result = pool.map(build_dict, cfg.options('OPTIONS'))

    # Map the parse()-function over each response in each option
    data = []
    for option in result:
        data += [parse(resp[0][0]) for category, resp in option.items()]

    print(data)

    print(len(data))

    # teacher = 3504
    # classes = 2534
    # rooms = 986