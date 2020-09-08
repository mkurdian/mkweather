import click

from mkweather import weather


@click.command(help='Displays the current weather.')
@click.option('--city', prompt='City', default='london', help='The name of the city to display weather for.')
@click.option('--country_code', prompt='Country Code', default='uk', help='The country code the city belongs to.')
def display_weather(city: str, country_code: str) -> None:
    output = weather.get_console_text(city=city, country_code=country_code)
    click.echo(output)


if __name__ == '__main__':
    display_weather()
