import requests

from dashboard.Image import draw_black, draw_red, get_enhanced_icon, h_red_image, small_font, medium_font
from dashboard.Config import open_weather_map_api_key, lat, lon, units, unit_letter


def print_weather():
	weather = get_weather()
	icon = get_enhanced_icon(weather['icon_path'], 45, False)
	h_red_image.paste(icon, (2, 32))
	draw_red.text(
		(50, 32),
		weather['current_temp'][0:2] + 'º' + unit_letter,
		font=medium_font,
		fill=0)
	draw_red.text(
		(50, 52),
		weather['description'],
		font=medium_font,
		fill=0)
	draw_black.text(
		(112, 32),
		'Feels like ' + weather['feels_like'][0:2] + 'º\n' +
		'Humidity ' + weather['humidity'][0:2] + '% ',
		font=small_font,
		fill=0)
	draw_black.text(
		(202, 32),
		'Day ' + weather['max_temp'][0:2] + 'º\n' +
		'Night ' + weather['min_temp'][0:2] + 'º',
		font=small_font,
		fill=0)


def get_weather():
	weather_url = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + lat + '&lon=' + lon + '&units=' + units + '&appid=' + open_weather_map_api_key
	weather = requests.get(weather_url)
	if weather.ok:
		weather_dictionary = weather.json()
		return {
			'description': str(weather_dictionary.get('current').get('weather')[0].get('main')),
			'current_temp': str(weather_dictionary.get('current').get('temp')),
			'min_temp': str(weather_dictionary.get('daily')[0].get('temp').get('min')),
			'max_temp': str(weather_dictionary.get('daily')[0].get('temp').get('max')),
			'icon_path': str(
				'assets/weather/' + weather_dictionary.get('current').get('weather')[0].get('icon') + '.png'),
			'feels_like': str(weather_dictionary.get('current').get('feels_like')),
			'humidity': str(weather_dictionary.get('current').get('humidity'))
		}
	else:
		return {}
