import os

import click
import requests


@click.command(help='Displays the current weather.')
@click.option('--city', prompt='City', default='london', help='The name of the city to display weather for.')
@click.option('--country_code', prompt='Country Code', default='uk', help='The country code the city belongs to.')
def display_weather(city: str, country_code: str) -> None:

    BOLD = "\033[1m"
    BOLD_END = "\033[0m"

    API_KEY = os.environ['OPEN_WEATHER_API_KEY']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&units=metric&appid={API_KEY}"
    r = requests.get(url)

    if r.ok:
        data = r.json()
    else:
        click.echo(r.json()['message'])
        return

    description = data['weather'][0]['description']
    temperature = data['main']['temp']

    output = f'''
        {BOLD}{city.lower().title()} Weather:{BOLD_END}

        Description: {description}
        Temperature: {temperature}˚C.
    '''
    click.echo(output)


if __name__ == '__main__':
    display_weather()
