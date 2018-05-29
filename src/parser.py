from .regex_patterns import *
from bs4 import BeautifulSoup
import datetime
import re


def parse(response, option):
    """
    Function to extract data from html schedule
    :return: Parsed html in dictionary
    """

    soup = BeautifulSoup(response.content, 'html.parser')

    title_blue_original = soup.find("font", {"color": "#0000FF"}).text.strip()

    if option != "classes" and option != "schedule":
        size = "4"
    else:
        size = "5"

    title_black_original = soup.find("font", {"size": size}).text.strip()
    title_blue_stripped = "".join(title_blue_original.split())[:-1]
    date = soup.find_all('font')[-1].get_text(strip=True)

    schedule = []

    rows = soup.find_all('table')[0].find_all('tr', recursive=False)[1:30:2]

    if option != "schedule":
        schedule.append(
            {'title_blue': title_blue_stripped, 'title_black': title_black_original})
    else:
        rowspans = {}
        for block, row in enumerate(rows, 1):
            daycells = row.select('> td')[1:]
            daynum, rowspan_offset = 0, 0
            for daynum, daycell in enumerate(daycells, 1):
                daynum += rowspan_offset
                while rowspans.get(daynum, 0):
                    rowspan_offset += 1
                    rowspans[daynum] -= 1
                    daynum += 1
                rowspan = (int(daycell.get('rowspan', default=2)) // 2) - 1
                if rowspan:
                    rowspans[daynum] = rowspan

                texts = daycell.find_all('font')
                if texts:
                    info = (item.get_text(strip=True) for item in texts)
                    seperated_info = get_separated_cell_info(info)
                    time = convert_date(date, daynum)
                    timetable = convert_timetable(block, block + rowspan)
                    schedule.append({
                        'abbrevation': title_blue_stripped,
                        'item': title_black_original,
                        'start_begin': timetable[0],
                        'start_end': timetable[1],
                        'start_block': block,
                        'end_begin': timetable[2],
                        'end_end': timetable[3],
                        'end_block': block + rowspan,
                        'daynum': daynum,
                        'day': time[0],
                        'date_full': time[1],
                        'date_year': time[1][0:4],
                        'date_month': time[1][5:7],
                        'date_day': time[1][8:10],
                        'info': seperated_info
                    })
                # print(schedule)
            while daynum < 5:
                daynum += 1
                if rowspans.get(daynum, 0):
                    rowspans[daynum] -= 1

        if not schedule:
            schedule = {}

    print("Page succesfully parsed")
    return schedule


def convert_date(soup_date, daynum):
    """
    Function to calculate day and date based on string and daynum
    :param soup_date: string containing the date of schedule page
    :param daynum: int of current day
    :return: tuple with current day and current date
    """

    days = {
        1: "Maandag",
        2: "Dinsdag",
        3: "Woensdag",
        4: "Donderdag",
        5: "Vrijdag"
    }

    one_day, one_month, one_year = soup_date[0:2], soup_date[3:5], soup_date[6:10]
    partials = [one_day, one_month, one_year]
    items = [int(i) for i in partials]

    d0 = datetime.date(year=items[2], month=items[1], day=items[0])

    current_day = days[daynum]
    current_date = d0 + datetime.timedelta(days=daynum - 1)

    return current_day, str(current_date)


def convert_timetable(start, end):
    """
    Function to convert rows to time
    :param start: Starting row number
    :param end: Ending row number
    :return: Tuple with all correct starting and ending times
    """

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

    start_begin = timetable[start][0]
    start_end = timetable[start][1]
    end_begin = timetable[end][0]
    end_end = timetable[end][1]

    return start_begin, start_end, end_begin, end_end


def compare_dicts(parsed_items, parsed_counters):
    """
    Function to combine parsed schedule data and quarter/week-info to a single dictionary
    :param parsed_items: defaultdict with nested lists containing separated dicts with crawled data per schedule
    :param parsed_counters: defaultdict with nested lists containing week and quarter per schedule
    :return: clean dictionary
    """
    print("Starting to build final dictionary")
    result = {}
    empty_schedules = 0
    for l1 in parsed_items:
        for option, (length, l2) in parsed_counters.items():
            if len(l1) == length:
                for item in zip(l1, l2):
                    schedule = bool(item[0])
                    if schedule:
                        quarter = item[1][0]
                        week = item[1][1]
                        result.setdefault(option, {})
                        result[option].setdefault(quarter, {})
                        result[option][quarter].setdefault(week, [])
                        result[option][quarter][week].append(item[0])
                    else:
                        empty_schedules += 1

    print("Succesfully builded final dictionary")
    print("{amount} schedules were empty.".format(amount=empty_schedules))
    return result


def get_separated_cell_info(cell_info):
    """
    Function to give each value in
    :param cell_info: generator that behaves like an iterator
    :return: category(key) of the reg_ex_dict and the matched value
    """
    seperated_info = {}
    for info in cell_info:
        # data contains
        # 1. a key from reg_ex_dict
        # 2. the value of the result after executing regular expressions on info
        data = get_category_and_result(info)
        if data is None:
            seperated_info["event"] = info
        elif data[0] == "location":
            dotSeperatedParts = data[1].split(".")
            seperated_info["building"] = dotSeperatedParts[0]
            seperated_info["floor"] = dotSeperatedParts[1]
            seperated_info["room"] = dotSeperatedParts[2]
        else:
            seperated_info[data[0]] = data[1]

    return seperated_info


def get_category_and_result(info):
    """
    Function to get the category(key) and the matched value after executing a regular expression
    :param info: info is a string
    :return: category(key) of the reg_ex_dict and the matched value
    """
    for category in reg_ex_dict:
        for pattern in reg_ex_dict[category]:
            match = re.match(pattern, info)
            if match:
                return category, match.group()
