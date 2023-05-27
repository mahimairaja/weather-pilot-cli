import requests
import json
from dotenv import load_dotenv
load_dotenv()

api_key = "Your API key"

city = "London"

link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"

'''
This is the working logic of the code
'''
response = requests.get(link)
data = json.loads(response.text)
print(data)