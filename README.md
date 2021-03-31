# `SimpleWeatherCLI`

![example workflow](https://github.com/kriogman/simpleweathercli/actions/workflows/python-publish.yml/badge.svg)

# Description

`simpleweathercli` is a simple command-line to find weather conditions in a city. It uses current and forecast data provided via API by https://openweathermap.org/. The purpose of this project is to create a simple example of a command-line interfaces using http://docopt.org/ and use Github Actions to build and upload the package to https://pypi.org/.

## Usage

```text
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
```

## Files

```text
simpleweathercli/
├── LICENSE
├── MANIFEST.in
├── README.md
├── setup.py
└── simpleweathercli
    ├── __init__.py
    └── cli.py
```

## Installation

Via PIP in your Python environment.

```bash
 pip install simpleweathercli
```

## API Key
You need an API Key from https://openweathermap.org/. In order to obtain an API Key you have to create an account, log in, go to https://home.openweathermap.org/api_keys and create an API Key. It's completely free and good enough for the purposes of this CLI.

## Examples

Note that these examples use a sample API key that is already disabled.

This first example will show the current data in a city.
 
```bash
simpleweathercli show --api-key=bb7dbc8217979c2c4f31eb0f9f1ceb94 Madrid
```
```text
{
    "base": "stations",
    "clouds": {
        "all": 0
    },
    "cod": 200,
    "coord": {
        "lat": 40.4165,
        "lon": -3.7026
    },
    "dt": 1617183561,
    "id": 3117735,
    "main": {
        "feels_like": 11.09,
        "humidity": 36,
        "pressure": 1023,
        "temp": 14.57,
        "temp_max": 16.67,
        "temp_min": 12
    },
    "name": "Madrid",
    "sys": {
        "country": "ES",
        "id": 6443,
        "sunrise": 1617170396,
        "sunset": 1617215859,
        "type": 1
    },
    "timezone": 7200,
    "visibility": 10000,
    "weather": [
        {
            "description": "clear sky",
            "icon": "01d",
            "id": 800,
            "main": "Clear"
        }
    ],
    "wind": {
        "deg": 50,
        "speed": 2.06
    }
}
```
This is an example with the forecast flag active. It will display weather forecast for 5 days with data every 3 hours by city name.
```bash
simpleweathercli show --forecast --api-key=90d91e149438f9d0a4f063dc5189720e London
```
```text
{
    "city": {
        "coord": {
            "lat": 51.5085,
            "lon": -0.1257
        },
        "country": "GB",
        "id": 2643743,
        "name": "London",
        "population": 1000000,
        "sunrise": 1617169064,
        "sunset": 1617215474,
        "timezone": 3600
    },
    "cnt": 40,
    "cod": "200",
    "list": [
        {
            "clouds": {
                "all": 44
            },
            "dt": 1617192000,
            "dt_txt": "2021-03-31 12:00:00",
            "main": {
                "feels_like": 17.35,
                "grnd_level": 1017,
                "humidity": 52,
                "pressure": 1021,
                "sea_level": 1021,
                "temp": 19.48,
                "temp_kf": -1.36,
                "temp_max": 20.84,
                "temp_min": 19.48
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "scattered clouds",
                    "icon": "03d",
                    "id": 802,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 206,
                "speed": 2.86
            }
        },
        
        ...
        
        {
            "clouds": {
                "all": 100
            },
            "dt": 1617613200,
            "dt_txt": "2021-04-05 09:00:00",
            "main": {
                "feels_like": -1.29,
                "grnd_level": 998,
                "humidity": 78,
                "pressure": 1001,
                "sea_level": 1001,
                "temp": 3.68,
                "temp_kf": 0,
                "temp_max": 3.68,
                "temp_min": 3.68
            },
            "pop": 1,
            "snow": {
                "3h": 1.14
            },
            "sys": {
                "pod": "d"
            },
            "visibility": 3550,
            "weather": [
                {
                    "description": "light snow",
                    "icon": "13d",
                    "id": 600,
                    "main": "Snow"
                }
            ],
            "wind": {
                "deg": 320,
                "speed": 4.3
            }
        }
    ],
    "message": 0
}

```
## Changelog

SimpleWeatherCLI Releases:

### 0.1.3

