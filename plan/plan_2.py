import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import json
import time
import csv
from geopy.distance import geodesic
import folium

rospy.init_node('flight_plan_with_csv_and_map')

get_telemetry = rospy.ServiceProxy('get_telemetry',srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
land = rospy.ServiceProxy('land', Trigger)

def wait_arrival(tolerance = 0.2):
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x**2 + telem.y**2+ telem.z**2) < tolerance:
            return
        rospy.sleep(0.2)

def load_plan_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def start_mission(mission):
    folium_map = folium.Map(location = [
        mission['mission']['plannedHomePosition'][0],
        mission['mission']['plannedHomePosition'][1],
    ],zoom_start=18)

    total_distance = 0
    points = []
    point_count = 0

    start_time = time.time()

    start_lat = mission['mission']['plannedHomePosition'][0]
    start_lon = mission['mission']['plannedHomePosition'][1]
    points.append((start_lat, start_lon, 3, 0))

    for item in mission['mission']['items']:
        command = item['command']
        altitude = item.get('Altitude', 3)

        if command == 22:
            navigate(x = 0, y = 0, z = altitude, frame_id = 'body', auto_arm = True)
            wait_arrival()

        if command == 16:
            lat = item['params'][4]
            lon = item['params'][5]
            speed = 0.5
            navigate_global(lat = lat, lon = lon, z = altitude, yaw = math.inf, speed = speed)
            wait_arrival()

            telem = get_telemetry(frame_id = 'navigate_target')
            points.append((telem.lat, telem.lon, telem.z, 0.5))
            point_count += 1

            folium.Marker(
                location=[telem.lat, telem.lon],
                popup=f'Lat: {telem.lat}\n Lon: {telem.lon}\n Alt: {telem.alt}\n Speed: {speed}'
            ).add_to(folium_map)

            if len(points) > 1:
                prev_point = points[-2]
                current_point = (telem.lat, telem.lon)
                distance = geodesic((prev_point[0], prev_point[1]), current_point).meters
                total_distance += distance

        elif command == 20:
            home_lat = mission['mission']['plannedHomePosition'][0]
            home_lon = mission['mission']['plannedHomePosition'][1]
            navigate_global(lat = home_lat, lon = home_lon, z = altitude, yaw = math.inf, speed = speed)
            wait_arrival()

            points.append((telem.lat, telem.lon, telem.z, 0.5))

            if len(points) > 1:
                prev_point = points[-2]
                current_point = (telem.lat, telem.lon)
                distance = geodesic((prev_point[0], prev_point[1]), current_point).meters
                total_distance += distance

        elif command == 21:
            land()
            points.append((telem.lat, telem.lon, telem.z, 0.5))

    locations = []
    for point in points:
        lat = point[0]
        lon = point[1]
        locations.append((lat, lon))

    folium.PolyLine(locations=locations, color='blue', weight = 2, opacity = 0.8).add_to(folium_map)


    end_time = time.time()
    total_time = end_time - start_time

    average_speed = total_distance / total_time

    folium_map.save("plan_flight_map.html")


    with open('flight_data_plan.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Lat', 'Lon', 'Alt', 'Speed'])
        for lat, lon, alt, speed in points:
            writer.writerow([lat, lon, alt, speed])

        writer.writerow(['total distance', total_distance]) 
        writer.writerow(['average_speed', average_speed]) 
        writer.writerow(['total_time', total_time]) 


mission_data = load_plan_file('plan2.plan')

start_mission(mission_data)