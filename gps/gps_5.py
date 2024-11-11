import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import csv

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


with open('telemetry.csv', mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['latitude', 'longitude', 'altitude'])

    start = get_telemetry()

    print(f'Start lat = {start.lat}, lon = {start.lon}')
    navigate_global(lat = start.lat, lon = start.lon, z = 3,  yaw = math.inf, speed = 0.5, auto_arm=True)
    wait_arrival()
    telem = get_telemetry()
    writer.writerow([telem.lat, telem.lon, telem.z])

    target_lat = 47.3977645
    target_lon = 8.5456126

    navigate_global(lat = target_lat, lon = target_lon, z = 3, yaw = math.inf, speed = 0.5)
    wait_arrival()

    telem = get_telemetry()
    writer.writerow([telem.lat, telem.lon, telem.z])

    navigate_global(lat = start.lat, lon = start.lon, z = 3, yaw = math.inf, speed = 0.5)
    wait_arrival()
    telem = get_telemetry()
    writer.writerow([telem.lat, telem.lon, telem.z])

    land()
