import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
from geopy.distance import geodesic

rospy.init_node('flight')

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

start = get_telemetry()
print(get_telemetry())
print(f'Start - lat = {start.lat}, lon = {start.lon}')

navigate(x = 0, y = 0, z = 3, frame_id = 'body', auto_arm = True)
wait_arrival()

target_lat = 47.3977320
target_lon = 8.5456438

navigate_global(lat = target_lat, lon = target_lon, z = start.z + 3, yaw = float('nan'), speed = 0.5)
wait_arrival()

land()

start_point = [start.lat, start.lon]
end_point = [target_lat, target_lon]
total_distance = geodesic(start_point, end_point).meters

print(total_distance)