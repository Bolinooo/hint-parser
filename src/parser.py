from bs4 import BeautifulSoup
import requests

link = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw3/14/t/t00050.htm"


def parse():
    """
    Function to extract data from html schedule
    :return: Parsed html in ???
    """

    resp = requests.get(link)
    soup = BeautifulSoup(resp.content, 'html.parser')

    title_blue = soup.find("font", {"color": "#0000FF"}).text.strip()
    title_black = soup.find("font", {"size": "4"}).text.strip()

    days = {
        1: "Maandag",
        2: "Dinsdag",
        3: "Woensdag",
        4: "Donderdag",
        5: "Vrijdag"
    }

    timetable = {
        1: ("8:30", "9:20"),
        2: ("9:20", "10:10"),
        3: ("10:30", "11:20"),
        4: ("11:20", "12:10"),
        5: ("12:10", "13:00"),
        6: ("13:00", "13:50"),
        7: ("13:50", "14:40"),
        8: ("15:00", "15:50"),
        9: ("15:50", "16:40"),
        10: ("17:00", "17:50"),
        11: ("17:50", "18:40"),
        12: ("18:40", "19:30"),
        13: ("19:30", "20:20"),
        14: ("20:20", "21:10"),
        15: ("21:10", "22:00"),
    }

    rows = soup.find_all('table')[0].find_all('tr', recursive=False)[1:30:2]

    rowspans = {}
    schedule = []

    for block, row in enumerate(rows, 1):
        daycells = row.select('> td')[1:] # skip td met tijd / eerste kolom
        rowspan_offset = 0
        for daynum, daycell in enumerate(daycells, 1):

            daynum += rowspan_offset
            while rowspans.get(daynum, 0):
                rowspan_offset += 1
                rowspans[daynum] -= 1
                daynum += 1
            rowspan = (int(daycell.get('rowspan', 2)) // 2) - 1

            if rowspan:
                rowspans[daynum] = rowspan

            texts = daycell.find_all('font')

            if texts:
                info = (item.get_text(strip=True) for item in texts)
                schedule.append({
                    'blok_start': block,
                    'blok_end': block + rowspan,
                    'day': daynum,
                    'info': [i for i in info]
                })

    return schedule