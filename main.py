import json

def load_restaurants(filename):
    with open(filename, 'r') as file:
        restaurants = json.load(file)
    return restaurants

def recommend_restaurant(restaurants, **filters):
    recommend_restaurants = []

    for restaurant in restaurants:
        match_criteria = True

        for key, value in filters.items():
            if key in restaurant:
                return 'working fine'
            


