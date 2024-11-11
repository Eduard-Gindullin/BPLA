import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import json

rospy.init_node('flight_plan')

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
    for item in mission['mission']['items']:
        command = item['command']
        altitude = item.get('Altitude', 3)

        if command == 22:
            navigate(x = 0, y = 0, z = altitude, frame_id = 'body', auto_arm = True)
            wait_arrival()
        
        elif command == 16:
            lat = item['params'][4]
            lon = item['params'][5]
            navigate_global(lat = lat, lon = lon, z = altitude, yaw = math.inf, speed = 0.5)
            wait_arrival()

        elif command == 20:
            home_lat = mission['mission']['plannedHomePosition'][0]
            home_lon = mission['mission']['plannedHomePosition'][1]
            navigate_global(lat = home_lat, lon = home_lon, z = altitude, yaw = math.inf, speed = 0.5)
            wait_arrival()

        elif command == 21:
            land()

mission_data = load_plan_file('plan2.plan')
start_mission(mission_data)
