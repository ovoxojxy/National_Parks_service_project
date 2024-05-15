import math

def distance(lat1, lon1, lat2, lon2):
    R = 6371.0

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat/ 2) **2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    return distance

lat_nyc = 40.7128
lon_nyc = -74.0060
lat_la = 34.0522
lon_la = -118.2437

distance_km = haversine_distance(lat_nyc, lon_nyc, lat_la, lon_la)
print(f"Distance between New York City and Los Angeles: {distance_km: .2f} km")
