from setuptools import setup

setup(
    name="weather_cli",
    version="0.1",
    packages=["weather_cli"],
    entry_points="""
        [console_scripts]
        wcli=weather_cli.get_weather:wcli
    """
)
