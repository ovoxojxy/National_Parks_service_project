import sys
import json
import math
import requests
from api_key import key
from api_key import google_key

# loads json file with local gainesville restaurants
def load_restaurants(filename):
    with open(filename, 'r') as file:
        restaurants = json.load(file)
    return restaurants

# returns restaurant matching user's desired cuisine
def match_cuisines(restaurants, user):

    matching_restaurants = []
    for restaurant in restaurants:
        if restaurant['cuisine'].lower() == user.lower():
            matching_restaurants.append(restaurant['name'])
    return matching_restaurants

#retrieves users ip address and returns approximate longitude and latitude coordinates
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response['ip']

def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/?key={key}').json()
    location_data = {
        # "ip" : ip_address,
        # "city": response.get("city"),
        # "region": response.get("region"),
        # "country": response.get("country_name"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude")
    }

    return location_data

#takes address and returns longitude and latitude coordinates
def get_coordinates(address):

    api_key = google_key
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    params = {
        'address': address,
        'key': api_key
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data['status'] == 'OK' and len(data['results']) > 0:
            location = data['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            return latitude, longitude
    except Exception as e:
        print('Error getting coordinates:', e)

    return None, None

#returns distance between two sets of longitude and latitude coordinate
def haversine_distance(lat1, lon1, lat2, lon2):
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
  
def main():
    GNV_restaurants = load_restaurants('restaurants.json')
    user_location = get_location()
    
    user_cuisine = str(input(
        "\nWhat cuisine of food would you like to eat?\nType the beginning of that food type and press enter to see if "
        "it's here.\n")).lower()
  
    print(match_cuisines(GNV_restaurants, user_cuisine))



if __name__ == '__main__':
    main()