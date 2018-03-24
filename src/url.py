from .decorator import *
from .helper import *


cfg = get_config('config.ini')

@validate_response
def get_response(url):
    """
    Function to return response code
    :param url: url to be checked
    :return: result of validate_response
    """
    return url


def build_set(option):

    # http://misc.hro.nl/roosterdienst/webroosters/CMI/kw3/13/c/c00001.htm

    base = cfg["URL"]["BASE"]
    quarter = cfg["SETTINGS"]["QUARTER"]
    education = cfg["SETTINGS"]["EDUCATION"]
    option = cfg["OPTIONS"][option]

    url = base + education + "/kw" + quarter + "/"


    return url