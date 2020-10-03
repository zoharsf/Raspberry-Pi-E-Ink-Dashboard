from PIL import ImageDraw, Image, ImageOps, ImageEnhance, ImageFont

from dashboard.Config import small_font_name, small_font_size, medium_font_name, medium_font_size, large_font_name, \
	large_font_size
from lib import epd2in7b

epd = epd2in7b.EPD()
epd.init()

h_black_image = Image.new('1', (epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH), 255)
draw_black = ImageDraw.Draw(h_black_image)

h_red_image = Image.new('1', (epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH), 255)
draw_red = ImageDraw.Draw(h_red_image)

small_font = ImageFont.truetype(small_font_name, small_font_size)
medium_font = ImageFont.truetype(medium_font_name, medium_font_size)
large_font = ImageFont.truetype(large_font_name, large_font_size)


def get_enhanced_icon(icon_path, size, invert):
	icon = Image.open(icon_path)
	icon = icon.resize((size, size))
	if invert:
		icon = ImageOps.invert(icon.convert('RGB'))
	else:
		icon = icon.convert('RGB')
	enhancer = ImageEnhance.Contrast(icon)
	icon = enhancer.enhance(2)
	icon.show()
	return icon
