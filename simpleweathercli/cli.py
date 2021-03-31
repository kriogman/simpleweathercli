"""
SimpleWeatherCLI
A command line tool to know the current and forecast weather data in a location.

Usage:
    simpleweathercli show [--forecast] (--api-key=APIKEY) <Location>
    simpleweathercli -h | --help
    simpleweathercli -v | --version

Options:
    -h, --help               Show this screen.
    -v, --version            Show version.

Command 'show' options:
        --api-key=APIKEY     A free & valid openweathermap API key.
        --forecast           Call 5 day / 3 hour forecast data.

"""
import requests
import json
import docopt
from simpleweathercli import __version__


def get_apikey(args):
    api_key = args['--api-key'] if '--api-key' in args else None
    return api_key


def response(api_request):
    r = requests.get(api_request)
    data = r.json()
    print(json.dumps(data, indent=4, sort_keys=True))


def main():

    args = docopt.docopt(__doc__)

    if args['--version']:
        print('simpleweathercli {}'.format(__version__))

    location = args['<Location>']
    api_key = get_apikey(args)

    if args['show']:

        if args['--forecast']:
            api_request = "https://api.openweathermap.org/data/2.5/forecast?q="\
                          + location + "&appid=" + api_key + "&units=metric"
            response(api_request)
        else:
            api_request = "https://api.openweathermap.org/data/2.5/weather?q="\
                          + location + "&appid=" + api_key + "&units=metric"
            response(api_request)


if __name__ == '__main__':
    main()
