import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import json

rospy.init_node('drone_control')

get_telemetry = rospy.ServiceProxy('get_telemetry',srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
land = rospy.ServiceProxy('land', Trigger)

# Ожидаем прибытие дрона к целевой позиции
def wait_arrival(tolerance = 0.2):
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x**2 + telem.y**2+ telem.z**2) < tolerance:
            return
        rospy.sleep(0.2)

# Загружаем план полета
def load_plan_file(filename):
    with open(filename, 'r') as file:
        plan = json.load(file)
    return plan

# Взлет на высоту 3 метра
def takeoff(navigate):
    print("Взлет на высоту 3 метра...")
    navigate(x = 0, y = 0, z = 3, frame_id = 'body', auto_arm = True)
    wait_arrival()
    print("Дрон взлетел")

# Посадка
def land_drone(land):
    print("Приземляемся...")
    land()
    print("Дрон приземлился")

# Полет по локальным координатам
def fly_to_local_coordinates(navigate):
    x = float(input("Введите координаты X (метры): "))
    y = float(input("Введите координаты Y (метры): "))
    print(f"Полет в точку X={x}, Y={y}")
    navigate(x = x, y = y, z = 0, frame_id = 'body', speed = 1)
    wait_arrival()
    print("Дрон достиг точки по локальным координатам")

# Полет по глобальным координатам
def fly_to_global_coordinates(navigate_global):
    lat = float(input("Введите широту: "))
    lon = float(input("Введите долготу: "))
    print(f"Полет в точку: Latitude={lat}, Longitude={lon}")
    navigate_global(lat = lat, lon = lon, z = 3, yaw = math.inf, speed = 1)
    wait_arrival()
    print("Дрон достиг точки по глобальным координатам")

# Запись домашней позиции
def record_home_position():
    telem = get_telemetry(frame_id = "body")
    home_position = (telem.lat, telem.lon)
    print(f"Домашняя позиция: Latitude={home_position[0]}, Longitude={home_position[1]}")
    return home_position

# Возврат на домашнюю позицию
def return_to_home(navigate_global, home_position):
    lat = home_position[0]
    lon = home_position[1]
    print(f"Возвращаемся на домашнюю позицию: Latitude={lat}, Longitude={lon}")
    navigate_global(lat = lat, lon = lon, z = 3, yaw = math.inf, speed = 1)
    wait_arrival()
    print("Дрон вернулся на домашнюю позицию")

# Полет по плану полета
def fly_by_plan(navigate_global, land):
    filename = input("Введите имя файла плана полета (например, plan.plan): ")
    plan = load_plan_file(filename)
    for item in plan['mission']['items']:
        command = item['command']
        if command == 16:
            lat = item['params'][4]
            lon = item['params'][5]
            print(f"Полет в точку: Latitude={lat}, Longitude={lon}")
            navigate_global(lat = lat, lon = lon, z = 3, yaw = math.inf, speed = 1)
            wait_arrival()
        elif command == 20:
            home_lat = plan['mission']['plannedHomePosition'][0]
            home_lon = plan['mission']['plannedHomePosition'][1]
            navigate_global(lat = home_lat, lon = home_lon, z = 3, yaw = math.inf, speed = 1)
            wait_arrival()
        elif command == 21:
            land()
            print("Дрон успешно приземлился")
            return False

# Основной цикл управления
def main():
    is_flying = False
    home_position = record_home_position()

    while True:
        print("\nВыберите действие:")
        print("1. Взлет (высота 3 метра)")
        print("2. Приземление")
        print("3. Полет по локальным координатам")
        print("4. Полет по глобальным координатам")
        print("5. Возврат на домашнюю позицию")
        print("6. Полет по плану полета")
        print("0. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            if not is_flying:
                takeoff(navigate)
                is_flying = True
            else:
                print("Дрон уже в воздухе")
        elif choice == '2':
            if is_flying:
                land_drone(land)
                is_flying = False
            else:
                print("Дрон уже на змеле")
        elif choice == '3':
            if is_flying:
                fly_to_local_coordinates(navigate)
            else:
                print("Сначала нужно взлететь")
        elif choice == '4':
            if is_flying:
                fly_to_global_coordinates(navigate_global)
            else:
                print("Сначала нужно взлететь")
        elif choice == '5':
            if is_flying:
                return_to_home(navigate_global, home_position)
        elif choice == '6':
            if is_flying:
                is_flying = fly_by_plan(navigate_global, land)
            else:
                print("Сначала нужно взлететь")
        elif choice == '0':
            print("Выход из программы")
            if is_flying:
                land_drone(land)
            break
        else:
            print("Неверный код команды")

main()