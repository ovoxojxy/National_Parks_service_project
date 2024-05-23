import sys
import json
import math
import requests
from restaurants import restaurant_data
from api_key import key
from api_key import google_key
from merge_sort_restaurants import merge_restaurants, merge_sort_restaurants, return_restaurants
from distance_sort import *
from welcome_page import *

# loads json file with local gainesville restaurants
def load_restaurants(filename):
    with open(filename, 'r') as file:
        restaurants = json.load(file)
    return restaurants

# global variable for restaurnt file
GNV_restaurants = load_restaurants('restaurants.json')
cuisines = ['american', 'bar & grill', 'bagel', 'barbecue', 'breakfast', 'brewery', 'caribbean', 'coffee', 'french', 'italian', 'southern', 'sushi', 'various']
# restaurants sorted by price
def get_restaurants_by_price(restaurant_list):
    restuarant_prices = []

    for restaurant in restaurant_list:
        restuarant_prices.append(GNV_restaurants[rest])

            
# returns restaurant matching user's desired cuisine
def match_cuisines(restaurants = restaurant_data, user_cuisine = None):

    matching_restaurants = []
    if user_cuisine in cuisines:
        for restaurant in restaurants:
            if restaurant['cuisine'].lower() == user_cuisine.lower():
                matching_restaurants.append(restaurant['name'])
    else:
        print('Category not available (Try entering: American, Bar & Grill, Barbecue, Breakfast, Brewery, Caribbean, Coffee, French, Italian, Southern, Sushi, Various)')
    
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

    return [location_data['latitude'], (-1 * location_data['longitude'])]

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
    distance = round(distance, 2)

    return (f'{distance} miles' )





  
def main():
    restaurant_distances = []
    restaurant_locations = {}
    user_location = get_location()
    result_dictionary_list = []

    print_welcome()
    show_intructions()
    
    user_cuisine = str(input(
        "\nWhat cuisine of food would you like to eat?\n ")).lower()
    
    user_sort_pref = str(input(
        "\nHow would you like your results sorted?:\nName, Distance, Ratings, or Price\n")).lower()

    results = match_cuisines(restaurant_data,user_cuisine)

    for result in results:
        for dictionary in restaurant_data:
            if result == dictionary['name']:
                result_dictionary_list.append(dictionary)

    for restaurant in result_dictionary_list:
        dist_from_rest = distance(user_location[0], user_location[1], restaurant['location'][0], restaurant['location'][1])
        restaurant_distances.append([restaurant['name'], dist_from_rest])


    if user_sort_pref == 'name':
        for dictionary in result_dictionary_list:
            print(dictionary['name'])
    elif user_sort_pref == 'price':
        merge_sort_restaurants(result_dictionary_list, 'price')
        return_restaurants(result_dictionary_list, 'price')
    elif user_sort_pref == 'ratings':
        merge_sort_restaurants(result_dictionary_list, 'ratings')
        rate_results = return_restaurants(result_dictionary_list, 'ratings')
    elif user_sort_pref == 'distance':
        merge_sort_distance(restaurant_distances)
        return_dist(restaurant_distances)
<<<<<<< HEAD

=======
>>>>>>> c87379100c2e66a05263889be56604860d3abd85
if __name__ == '__main__':
    main()
