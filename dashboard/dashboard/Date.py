import datetime

from dashboard.Image import draw_black, draw_red, medium_font, large_font
from dashboard.Dictionaries import months, date_suffix, weekdays


def print_date():
	date = get_date()
	w, h = draw_red.textsize(date['weekday'], font=large_font)
	draw_red.text((2, 2),
				  date['weekday'],
				  font=large_font,
				  fill=0)
	draw_black.text((w + 7, 5),
					months[date['month']] + ' ' + date['day'] + date_suffix[date['day']] + ' ' + date['year'],
					font=medium_font,
					fill=0)


def get_date():
	now = datetime.datetime.now()
	return {
		'weekday': weekdays[str(now.isoweekday())],
		'day': str(now.day),
		'month': str(now.month),
		'year': str(now.year)
	}
