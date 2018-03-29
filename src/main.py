from .parser import *
from .url import *

def main():

    link = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw3/14/t/t00050.htm"


    resp = requests.get(link)
    soup = BeautifulSoup(resp.content, 'html.parser')

    convert_dates(soup)

    # item = parse()

    #
    #
    #
    # for nr, i in sorted(enumerate(item)):
    #     print(i)

    # links = build_dict()

    # extracted_links = [[i for i in links[key]] for key in links.keys()]

    # for link in links.values():
    #     print(len(link))

    # teacher = 3504
    # classes = 2534
    # rooms = 986