from dotenv import load_dotenv
load_dotenv()
import os

# weather
icon_base_url = 'http://openweathermap.org/img/wn/'
open_weather_map_api_key = os.environ.get("open_weather_map_api_key")
lat = os.environ.get("lat")
lon = os.environ.get("lon")
units = 'imperial'
unit_letter = 'F'

# covid
country = 'us'
covid_url = 'https://corona.lmao.ninja/v2/'

# fonts
small_font_size = 14
medium_font_size = 19
large_font_size = 24

small_font_name = '/home/pi/.fonts/Rubik-Light.ttf'
medium_font_name = '/home/pi/.fonts/Rubik-Regular.ttf'
large_font_name = '/home/pi/.fonts/Rubik-Bold.ttf'
