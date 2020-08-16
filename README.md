# mkweather

A python package to request weather data from the [OpenWeather web API](https://openweathermap.org/).

## Usage

**API Key**

You will need an API key to use this package.

1. Register for an account at [openweathermap.org](https://openweathermap.org/) to obtain an API key.
1. Within the root folder, create a `.env` file with the following content, replacing everything after the `=` with your API key:

```
OPEN_WEATHER_API_KEY={your api key goes here}
```

**Install Package**

`pipenv install .`

**Run**

`pipenv run python main.py`

**Get Help**

`pipenv run python main.py --help`

```
Usage: main.py [OPTIONS]

  Displays the current weather.

Options:
  --city TEXT          The name of the city to display weather for.
  --country_code TEXT  The country code the city belongs to.
  --help               Show this message and exit.
```

## Developer Mode and Unit Tests

**Install in Developer Mode**

`pipenv install -e . --dev`

**Run Tests**

`pipenv run pytest -v`

**Integration Tests with Live Web API**

Unit tests that hit the live OpenWeather web API are skipped by default. To test the contract with the live API, set the `SKIP_INTEGRATION_TEST` environment variable to `False` by pasting the following line into your `.env` file:

`SKIP_INTEGRATION_TEST=False`
