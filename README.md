# Birmingham Uni timetable extractor

The University of Birmingham has a lovely service for accessing timetables
that is completely incompatible with any reasonable system. This is a simple
command line tool to extract the data from my.bham and generate something
compatible with a reasonable system.

This project is inspired (and takes a bit of code from) [Tom Moses](https://github.com/tomhmoses)'
work on [OnlineBhamTimetableConverter][timetable-converter]. It's a great
project, however, I'm generally unhappy about having to give my password off
to third-party services, and I just need a simple command line tool.

## Installation

bhamcal requires at least python 3.7, as it uses some slightly more modern
features.

Additionally, chromedriver is required for selenium to scrape the calendar
data. To install it, see [here][selenium-install] (for windows-specific
instructions, see below).

Finally, to actually install bhamcal, clone the repository, and install it
using pip:

    $ git clone https://github.com/jedevc/bhamcal.git
    $ cd bhamcal
    $ pip3 install -e .

If you don't want to install it system-wide, you can run it as a module, after
installing the dependencies:

    $ pip install -r requirements.txt
    $ python3 -m bhamcal

### Windows

- Download `chromedriver.exe` from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- Put it inside `C:\Windows`.

## Usage

To generate a calendar format:

    $ bhamcal <username> -o calendar.ics

For other options, see the help:

    $ bhamcal --help

### Output formats

bhamcal can output calendars in a variety of different formats. However, each
has it's own instructions and quirks.

#### iCalendar

iCalendar is the default, recommended output format. It's the most
comprehensive, feature-full format out there for calendars and is understood
by almost all calendar software.

To generate an iCalendar:

    $ python -m bhamcal <username> -f ical -o calendar.ics

#### CSV

CSV outputs are the simplest in terms of complexity, and should be accepted
in most places, however, they don't contain the full complexity that
iCalendar can and should only be used when iCalendar is not available.

To generate a CSV:

    $ python -m bhamcal <username> -f csv -o calendar.csv

#### Google Calendar

Google Calendar outputs are the most complicated to setup.

First we need to setup a Google Cloud project so we can access the Google
Calendar API:

1. [Create a new Google Cloud project](https://console.cloud.google.com/projectcreate)
2. [Enable the Google Calendar API](https://console.cloud.google.com/apis/api/calendar-json.googleapis.com/overview)
3. [Modify the OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent)
4. [Create an OAuth client ID credential](https://console.cloud.google.com/apis/credentials)
    - Download the credentials in JSON format and place them in your current
    directory as `credentials.json`.
5. Run the application (using the command below), following the link to
generate an OAuth token.
6. Wait until the calendar is finished uploading!

To generate a Google Calendar:

    $ python -m bhamcal <username> -f gcal -o <calendarId>

The Calendar ID can be found in the calendar-specific settings in the Google
Calendar web view.

## Development

To develop, first set up the pipenv:

    $ pipenv shell

Then, you can run the tool using:

    $ python -m bhamcal

If you add new dependencies, make sure that they are reflected in both
`requirements.txt` and `setup.py`.

## License

This project is licensed under the GPLv3. Enjoy! :tada:

[timetable-converter]: https://github.com/tomhmoses/OnlineBhamTimetableConverter
[selenium-install]: https://selenium-python.readthedocs.io/installation.html
