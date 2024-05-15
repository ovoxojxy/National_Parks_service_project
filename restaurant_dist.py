from distance_formula import haversine_distance
from restaurants import restaurant_data

def store_user_dist(res, user_lat, user_long, res_lat, res_long):
    
    distances = {}
    
    for restaurant in res:
        distances[restaurant] = distance(user_lat, user_long, res_lat, res_long)

    return distances

store_user_dist()