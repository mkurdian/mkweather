import os

import requests


def display_weather(city: str, country_code: str) -> None:

    BOLD = "\033[1m"
    BOLD_END = "\033[0m"

    API_KEY = os.environ['OPEN_WEATHER_API_KEY']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&units=metric&appid={API_KEY}"
    r = requests.get(url)

    if r.ok:
        data = r.json()
    else:
        print(r.json()['message'])
        return

    description = data['weather'][0]['description']
    temperature = data['main']['temp']

    output = f'''
        {BOLD}{city.lower().title()} Weather:{BOLD_END}

        Description: {description}
        Temperature: {temperature}˚C.
    '''
    print(output)


if __name__ == '__main__':
    display_weather(city="london", country_code="uk")
