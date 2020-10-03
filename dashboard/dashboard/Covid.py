import requests

from dashboard.Image import draw_black, get_enhanced_icon, h_black_image, h_red_image, small_font
from dashboard.Config import country, covid_url


def get_covid(url_suffix):
	current_covid = requests.get(covid_url + url_suffix)
	if current_covid.ok:
		current_covid_dictionary = current_covid.json()
		return {
			'total_cases': str("{:,}".format(current_covid_dictionary.get('cases'))),
			'today_cases': str("{:,}".format(current_covid_dictionary.get('todayCases'))),
			'active_cases': str("{:,}".format(current_covid_dictionary.get('active'))),
			'deaths': str("{:,}".format(current_covid_dictionary.get('deaths'))),
			'today_deaths': str("{:,}".format(current_covid_dictionary.get('todayDeaths'))),
		}
	else:
		return {}


def print_covid():
	covid_global = get_covid('all')
	covid_local = get_covid('countries/' + country)

	covid_icon = get_enhanced_icon('assets/covid/covid.jpeg', 45, False)
	global_icon = get_enhanced_icon('assets/covid/globe.jpeg', 25, False)
	local_icon = get_enhanced_icon('assets/covid/' + country + '.jpeg', 25, False)
	cough_icon = get_enhanced_icon('assets/covid/cough.jpeg', 22, False)
	skull_icon = get_enhanced_icon('assets/covid/skull.jpeg', 22, False)

	h_red_image.paste(covid_icon, (2, 80))
	h_black_image.paste(global_icon, (50, 90))
	h_black_image.paste(cough_icon, (82, 80))
	h_black_image.paste(skull_icon, (78, 102))
	draw_black.text(
		(110, 85),
		covid_global['total_cases'].rsplit(',', 2)[0] + '.' + covid_global['total_cases'].rsplit(',', 2)[1][:1] + 'M',
		font=small_font,
		fill=0)
	draw_black.text(
		(110, 105),
		covid_global['deaths'].rsplit(',', 2)[0] + '.' + covid_global['deaths'].rsplit(',', 2)[1][:2] + 'M',
		font=small_font,
		fill=0)

	h_black_image.paste(local_icon, (160, 90))
	h_black_image.paste(cough_icon, (192, 80))
	h_black_image.paste(skull_icon, (188, 102))
	draw_black.text(
		(218, 85),
		covid_local['total_cases'].rsplit(',', 2)[0] + '.' + covid_local['total_cases'].rsplit(',', 2)[1][:2] + 'M',
		font=small_font,
		fill=0)
	draw_black.text(
		(218, 105),
		'0.' + covid_local['deaths'].rsplit(',', 2)[0][:2] + 'M',
		font=small_font,
		fill=0)
