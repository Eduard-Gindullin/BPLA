import folium

def create_map():
    return folium.Map(location=[47.3977418, 8.5455938], zoom_start=18)

def update_light_path(map_drone, drone_position):
    folium.PolyLine(locations=drone_position, color='blue', weight=2.5, opacity=1).add_to(map_drone)

def save_map(map_drone):
    map_drone.save("map_drone.html")
    print("Карта сохранена как map_drone.html")