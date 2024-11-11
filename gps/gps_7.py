import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import folium
from geopy.distance import geodesic

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry',srv.GetTelemetry)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
land = rospy.ServiceProxy('land', Trigger)

def wait_arrival(tolerance = 0.2):
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x**2 + telem.y**2+ telem.z**2) < tolerance:
            return
        rospy.sleep(0.2)

start = get_telemetry()

print(get_telemetry())

navigate_global(lat = start.lat, lon = start.lon, z = 3, yaw = math.inf, speed = 0.5, auto_arm=True)
wait_arrival()

waypoints = [
    (47.3977396, 8.5456843),
    (47.3977986, 8.5456932),
    (47.3978223, 8.5455800)
]

total_distance = 0
current_position = (start.lat, start.lon)

for target_lat, target_lon in waypoints:
    navigate_global(lat = target_lat, lon = target_lon, z = start.z +3, yaw = math.inf, speed = 1)
    wait_arrival()

    distance = geodesic(current_position, (target_lat, target_lon)).meters
    total_distance += distance
    current_position = (target_lat, target_lon)

total_distance +=geodesic(current_position, (start.lat, start.lon)).meters

map_flight_distance = folium.Map(location=[start.lat, start.lon], zoom_start=18)
takeoff_marker = folium.Marker(
    [start.lat, start.lon],
    popup=f"Takeoff\n lat {start.lat} lon {start.lon}",
    icon=folium.Icon(color="green")
).add_to(map_flight_distance)

landing_marker = folium.Marker(
    [start.lat, start.lon],
    popup=f"Land\ntotal distance {total_distance} m",
    icon=folium.Icon(color="blue")
).add_to(map_flight_distance)

folium.PolyLine([(start.lat,start.lon)] + waypoints,color='red', weight=2.5, opacity = 1).add_to(map_flight_distance)

navigate_global(lat = start.lat, lon = start.lon, z = start.z + 3, yaw = math.inf, speed = 1)
wait_arrival()
map_flight_distance.save('map_flight_distance.html')

land()