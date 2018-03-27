from bs4 import BeautifulSoup
from .url import *
import re
import requests

link = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw3/14/t/t00050.htm"


def parse():

    resp = requests.get(link)
    soup = BeautifulSoup(resp.text, 'html.parser')

    title_blue = soup.find("font", {"color": "#0000FF"}).text.strip()
    title_black = soup.find("font", {"size": "4"}).text.strip()

    # dagen
    for row in soup.find("table").find_all("tr")[1:7]:
        columns = row.find_all("td")
        for col in columns:
            col = (col.text.strip())
            if col:
                print(col)



