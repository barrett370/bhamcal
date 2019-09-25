# Birmingham Uni timetable extractor

The University of Birmingham has a lovely service for accessing timetables
that is completely incompatible with any reasonable system. This is a simple
command line tool to extract the data from my.bham and generate something
compatible with a reasonable system.

This project is inspired (and takes a bit of code from) [Tom Moses](https://github.com/tomhmoses)'s
work on [OnlineBhamTimetableConverter][timetable-converter]. It's a great
project, however, I'm generally unhappy about having to give my password off
to third-party services, and I just need a simple command line tool.

## Installation

bhamcal requires at least python 3.7, as it uses some slightly more modern
features.

Additionally, chromedriver is required for selenium to scrape the calendar
data - to install it, see [here][selenium-install].

Finally, to actually install bhamcal, clone the repository, and install it
using pip:

    $ git clone https://github.com/jedevc/bhamcal.git
    $ cd bhamcal
    $ pip3 install -e .

### Windows

Put the `chromedriver.exe` inside `C:\Windows`.

## Usage

To generate a calendar in iCal format:

    $ bhamcal <username> -o calendar.ical

For other options, see the help:

    $ bhamcal --help

## Development

To develop, first set up the pipenv:

    $ pipenv shell

Then, you can run the tool using:

    $ python -m bhamcal

## License

Like [OnlineBhamTimetableConverter][timetable-converter], this project is
licensed under the GPLv3. Enjoy! :tada:

[timetable-converter]: https://github.com/tomhmoses/OnlineBhamTimetableConverter
[selenium-install]: https://selenium-python.readthedocs.io/installation.html