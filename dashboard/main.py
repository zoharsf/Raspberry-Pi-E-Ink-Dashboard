import time

from dashboard.Covid import print_covid
from dashboard.Date import print_date
from dashboard.Image import epd, h_black_image, h_red_image
from dashboard.Speed import print_speed
from dashboard.Weather import print_weather


def gather_data():
	print("Gathering data:")
	print("\tGathering date data... ", end='')
	tic = time.perf_counter()
	print_date()
	toc = time.perf_counter()
	print(f"took {toc - tic:0.4f} seconds")
	print("\tGathering weather data... ", end='')
	tic = time.perf_counter()
	print_weather()
	toc = time.perf_counter()
	print(f"took {toc - tic:0.4f} seconds")
	print("\tGathering covid data... ", end='')
	tic = time.perf_counter()
	print_covid()
	toc = time.perf_counter()
	print(f"took {toc - tic:0.4f} seconds")
	print("\tGathering speed data... ", end='')
	tic = time.perf_counter()
	print_speed()
	toc = time.perf_counter()
	print(f"took {toc - tic:0.4f} seconds")


def print_data():
	print("Printing to screen:")
	print("\tClearing screen... ", end='')
	tic = time.perf_counter()
	epd.Clear()
	toc = time.perf_counter()
	print(f"took {toc - tic:0.4f} seconds")
	print("\tWriting to screen... ", end='')
	tic = time.perf_counter()
	epd.display(epd.getbuffer(h_black_image), epd.getbuffer(h_red_image))
	toc = time.perf_counter()
	print(f"took {toc - tic:0.4f} seconds")


def main():
	gather_data()
	print_data()


if __name__ == "__main__":
	main()
