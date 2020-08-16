import requests
from datetime import datetime
from typing import Optional
from urllib.parse import urljoin

from mkweather.constants import BASE_URL, API_KEY, BOLD, BOLD_END


def get_weather(city: str, country_code: str) -> Optional[requests.Response]:
    """
    Request current weather from web API.
    """
    parameters = {
        'q': f'{city},{country_code}',
        'units': 'metric',
        'appid': API_KEY
    }
    URL = urljoin(BASE_URL, 'weather')

    response = requests.get(URL, params=parameters)

    if response.ok:
        return response
    else:
        return None


def get_console_text(city: str, country_code: str) -> str:
    """
    Return console display string for current weather output.
    """
    response = get_weather(city=city, country_code=country_code)

    if response is None:
        return "Failed request."
    else:
        json_response = response.json()

        location = f"{json_response['name']}, {json_response['sys']['country']}"
        description = json_response['weather'][0]['description']
        temperature = json_response['main']['temp']
        date_time = datetime.fromtimestamp(
            json_response['dt'] + json_response['timezone'])

        return f"""\n{BOLD}Weather:{BOLD_END}\n{location} {date_time.strftime('%a %b %Y %H:%M')}\n{temperature}˚C\n{description}"""
