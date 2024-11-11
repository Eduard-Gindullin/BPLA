import rospy
from clover import srv
from std_srvs.srv import Trigger
import math


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

center_lat = 47.3977752
center_lon = 8.5457071
radius = 0.0001

for angle in range(0, 360, 30):
    target_lat = center_lat + radius * math.cos(math.radians(angle))
    target_lon = center_lon + radius * math.sin(math.radians(angle))
    navigate_global(lat = target_lat, lon = target_lon, z = 3, yaw = math.inf, speed = 1)
    wait_arrival()

land()