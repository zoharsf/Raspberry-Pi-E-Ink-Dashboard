import json
import subprocess

from dashboard.Image import draw_black, get_enhanced_icon, h_black_image, h_red_image, small_font


def print_speed():
	speed = get_speed()

	odometer_icon = get_enhanced_icon('assets/speed/odometer.jpeg', 45, False)
	download_icon = get_enhanced_icon('assets/speed/download.jpeg', 25, False)
	upload_icon = get_enhanced_icon('assets/speed/upload.jpeg', 25, False)

	h_red_image.paste(odometer_icon, (2, 128))
	h_black_image.paste(download_icon, (50, 138))
	draw_black.text(
		(82, 140),
		speed['download'] + 'Mbps',
		font=small_font,
		fill=0)

	h_black_image.paste(upload_icon, (160, 138))
	draw_black.text(
		(190, 140),
		speed['upload'] + 'Mbps',
		font=small_font,
		fill=0)


def get_speed():
	result = subprocess.run(['speed-test', '-j'], stdout=subprocess.PIPE)
	result_dictionary = json.loads(result.stdout.decode('utf-8'))
	return {
		'ping': str(result_dictionary.get('ping')),
		'download': str(result_dictionary.get('download')),
		'upload': str(result_dictionary.get('upload'))
	}
