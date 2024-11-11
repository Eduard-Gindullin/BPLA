import csv
import folium

filename = '/home/clover/catkin_ws/Code/tele/telemetry2.csv'


latitude_values = []
longitude_values = []

# Открытие csv в режиме для чтения
with open(filename, 'r') as file:
    csv_reader = csv.reader(file, delimiter=';')

    # Чтение заголовков
    headers = next(csv_reader)
    print("Заголовки",headers)

    # Чтение данных построчно
    for row in csv_reader:
        if row:
            latitude_values.append(float(row[1]))
            longitude_values.append(float(row[2]))

center_lat = sum(latitude_values) / len(latitude_values)
center_lon = sum(longitude_values) / len(longitude_values)

m = folium.Map(location=[center_lat, center_lon], zoom_start=18)

data = []

for i in range(len(latitude_values)):
    lat = latitude_values[i]
    lon = longitude_values[i]
    coordinates = [lat, lon]

    data.append(coordinates)


folium.PolyLine(data, color='blue', weight=2.5, opacity=1).add_to(m)
m.save("map.html")    