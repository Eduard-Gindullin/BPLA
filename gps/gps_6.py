import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import folium

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
map_flights = folium.Map(location=[start.lat, start.lon],zoom_start=18)
coordinates = []
low_alt = []

navigate_global(lat = start.lat, lon = start.lon, z = 3, yaw = math.inf, speed = 0.5, auto_arm=True)
wait_arrival()

waypoints = [
    (47.3977843, 8.5456743),
    (47.3978226, 8.5456387),
    (47.3978200, 8.5455634),
    (47.3977987, 8.5455052),
    (47.3977548, 8.5455261),
    (47.3977370, 8.5455675)
]

for target_lat, target_lon in waypoints:
    navigate_global(lat = target_lat, lon = target_lon, z = start.z + 3, yaw = math.inf, speed = 0.5)
   
    while True:
        current_telem = get_telemetry()
        coordinates.append((current_telem.lat, current_telem.lon))

        if current_telem.z < 3:
            if (current_telem.lat, current_telem.lon) not in low_alt:
                folium.Marker(
                    location = (current_telem.lat, current_telem.lon),
                    popup = f"altitude {current_telem.z}",
                    icon=folium.Icon(color="red")
                ).add_to(map_flights)
                low_alt.append((current_telem.lat, current_telem.lon))

        if math.sqrt((current_telem.lat - target_lat)**2 + (current_telem.lon - target_lon)**2) < 0.00001:
            break

folium.PolyLine(coordinates, color="blue", weight=1.5, opacity = 1).add_to(map_flights)

land()

map_flights.save("map_flights2.html")