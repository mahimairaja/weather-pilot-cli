import click
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    api_key = os.getenv('secret')
    

@click.command()
@click.option("--city", prompt="City name", help="Enter city name")
def wcli(city):
    """Display the weather of a city."""
    data = getWeather(city)
    weather = data['weather'][0]['description']
    temp = data['main']['temp'] - 273.15
    click.echo("Weather report for " + city)
    click.echo(f"Sky : {weather}")
    click.echo(f"Temperature: {temp : .2f}•C")


@click.group()
def cli():
    pass

def getWeather(city):
    api_key = os.getenv('secret')
    link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
    response = requests.get(link)
    data = json.loads(response.text)
    return data

if __name__ == "__main__":  
    cli.add_command(wcli)