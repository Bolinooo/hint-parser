from .decorator import *
import requests

@validate_response
def get_response(url):
    return url
