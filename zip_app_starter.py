import zip_util
import math 

zip_codes = zip_util.read_zip_all("zip_codes_states.csv")

def calculate_distance(zip_codes):
	"""
	Функция calculate_distance принимает данные двух точек на земной поверхности
	Каждая точка - это кортеж вида (широта, долгота)
	
	Возвращаемое значение - расстояние в милях (число с плавающей точкой) по земной поверхности между двумя заданными точками
	"""
	zip1 = input("Enter the first ZIP Code => ").strip()
	print(zip1)
	zip2 = input("Enter the second ZIP Code => ").strip()
	print(zip2)
	loc1 = []
	loc2 = []
	for i in range(len(zip_codes)):
		if zip_codes[i][0] == zip1:
			loc1.extend([zip_codes[i][1],zip_codes[i][2]])
		elif zip_codes[i][0] == zip2:
			loc2.extend([zip_codes[i][1],zip_codes[i][2]])
	if len(loc1) == 0 or len(loc2) == 0:
		print(f"Error: ZIP code not found")
		return
	
	R = 6371.0
	lat1 = math.radians(loc1[0])
	lon1 = math.radians(loc1[1])
	lat2 = math.radians(loc2[0])
	lon2 = math.radians(loc2[1])
	
	dlat = lat2 - lat1
	dlon = lon2 - lon1

	count1 = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
	count2 = 2 * math.atan2(math.sqrt(count1), math.sqrt(1 - count1))
	dist = R * count2
	print(f"The distance between {zip1} and {zip2} is {dist*0.621371:.2f} miles")

def location_by_zip(zip_codes, zip_code):
	"""
	Функция location_by_zip находит все данные по индексу, указанному в zip_code
	Возвращаемое значение - это кортеж вида (latitude, longitude, city, state, county)
	"""
	pass

def coordinates_count(coordinates,coord_type):
	degrees = int(abs(coordinates))
	minutes_full = (abs(coordinates) - degrees) * 60
	minutes = int(minutes_full)
	seconds = (minutes_full - minutes) * 60

	if coord_type == 'lat':
		direction = 'N' if coordinates >= 0 else 'S'
	elif coord_type == 'lon':
		direction = 'E' if coordinates >= 0 else 'W'
	
	return degrees, minutes, seconds, direction

def process_loc(zip_codes):
	"""
	Функция process_loc() принимает список списков с данными о всех индексах и
	реализует обработку команды loc.
	"""
	# 1. Запросить индекс у пользователя и сохранить в переменной zip_code
	zip_code = input('Enter a ZIP Code to lookup => ').strip()
	print(zip_code)
	
	line = 0
	# 2. Найти данные по индексу или напечатать сообщение об ошибке, если такого индекса нет
	for i in range(len(zip_codes)):
		if zip_codes[i][0] == zip_code:
			line = i
			break
	else:
		print(f"Error: ZIP Code not found")
		return
	
	coordinates = zip_codes[line][1]
	#print(coordinates)
	lattitude = coordinates_count(coordinates,'lat')

	coordinates = zip_codes[line][2]
	#print(coordinates)
	longitude = coordinates_count(coordinates,'lon')
	#print(lattitude)
	#print(longitude)
	print(f"ZIP Code {zip_code} is in {zip_codes[line][3]}, {zip_codes[line][4]}, {zip_codes[line][5]} county,\ncoordinates: ({lattitude[0]:03d}°{lattitude[1]}'{lattitude[2]:.2f}\"{lattitude[3]},{longitude[0]:03d}°{longitude[1]}'{longitude[2]:.2f}\"{longitude[3]})")


def process_zip(zip_codes):
	city = str(input('Enter a city name to lookup => ')).strip()
	print(city)
	state = str(input('Enter the state name to lookup => ')).strip()
	print(state)

	city = city.lower()
	state = state.lower()
	zips = []
	for i in range(len(zip_codes)):
		if zip_codes[i][3].lower() == city and zip_codes[i][4].lower() == state:
			zips.append(zip_codes[i][0])
			#print(zips)

	if len(zips) != 0 :
		print(f"The following ZIP Code(s) found for {city.title()}, {state.upper()}: {", ".join(zips)}")	
	else:
		print("Error: city and/or state not found.")


def main_loop():
	while True:
		cmd = input("Command ('loc', 'zip', 'dist', 'end') => ").strip()
		cmd = cmd.lower()
		if cmd == 'end':
			print("Done")
			break
		elif cmd == 'loc':
			process_loc(zip_codes)
		elif cmd == 'zip':
			process_zip(zip_codes)
		elif cmd == 'dist':
			calculate_distance(zip_codes)
		else:
			print(f"Invalid command, ignoring")
			
				


if __name__ == '__main__':
	main_loop()
