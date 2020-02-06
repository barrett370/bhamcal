import re
from datetime import datetime

import pytz
from bs4 import BeautifulSoup

from .event import CalendarEvent

DEFAULT_TIMEZONE = pytz.timezone('Europe/London')

cheats = {
        "LH Nature Inspired Search and Optimisation/LM Advanced Aspects of Nature-Inspired Search and Optimisation(28209/32235)": 
        "Aspects of Nature Inspired Search and Optimisation"
}


def extract(frame):
    soup = BeautifulSoup(frame, 'html.parser')
    spreadsheets = soup.find_all('table', class_='spreadsheet')

    for spreadsheet in spreadsheets:
        rows = spreadsheet.find_all('tr')[1:]
        for row in rows:
            yield extract_event(row)


def extract_event(table_row):
    entries = table_row.find_all('td')
    entries = [entry.string.strip() for entry in entries]

    # extract data from table
    day = entries[0]
    title = entries[1].strip()
    event_type: str = entries[2]
    start_time = entries[3]
    end_time = entries[4]
    location = entries[5]
    lecturer = entries[6]
    department = entries[7]

    # process subject title
    match = re.match("(.+)\((\d+)\)/", title)
    if match:
        name = match.group(1)
        code = match.group(2)
    else:
        match = re.match("(.+)/", title)
        if match:
            name = match.group(1)
            code = name.upper().replace(' ', '')
        else:
            name = title
            code = title.upper().replace(' ', '')

    if event_type.__contains__("/"):
        event_type = event_type.split("/")[0]
    if name in cheats.keys():
        print(f"Found cheat for {name}")
        name = f"[{event_type}] - {cheats[name]}"
    else:
        name = f"[{event_type}] - {clean_subject(name)}"
    print(name)
    # build description
    description = ""
    description += 'With: ' + lecturer + '\n'
    description += 'Activity: ' + title + '\n'
    description += 'Type: ' + event_type + '\n'
    description += 'Department: ' + department

    return CalendarEvent(
        start=extract_datetime(day, start_time),
        end=extract_datetime(day, end_time),
        subject=name,
        subject_code=code,
        event_type=event_type,
        location=location,
        description=description
    )


def extract_datetime(date, time):
    dt = datetime.strptime(date + " " + time, "%d %b %Y %H:%M")
    dt = DEFAULT_TIMEZONE.localize(dt)
    dt = dt.astimezone(pytz.utc)
    return dt


# Remove module codes, LM and/or LH and extended.
CODE_STRIPPER = re.compile(
    r"(?P<code>\([0-9]+/[0-9]+\))|(?P<prefix>LM/LH|LH/LM|LH|LM|LI)|(?P<extended>\(Extended\)?)"
)
# Remove duplicates in the case of the name being present twice on some extended modules.
REMOVE_DOUBLES = re.compile(
    r"(?P<one>^.*/)"
)


def clean_subject(subject: str) -> str:
    subject = re.sub(CODE_STRIPPER, "", subject)
    items = subject.split("/")
    if len(items) == 2:
        if items[0].lower().strip() == items[1].lower().strip():
            subject = re.sub(REMOVE_DOUBLES, "", subject)
    subject = re.sub(r'\(\)',"",subject)
    return subject.strip()
