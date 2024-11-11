import csv

filename = '/home/clover/catkin_ws/Code/tele/telemetry.csv'

data = []
headers = []

# Открытие csv в режиме для чтения
with open(filename, 'r') as file:
    csv_reader = csv.reader(file, delimiter=';')

    # Чтение заголовков
    headers = next(csv_reader)
    print("Заголовки",headers)

    # Чтение данных построчно
    for row in csv_reader:
        if row:
            data.append(row)

print("Пример строки:", data[0])
for column in data:
    print(column[6])
