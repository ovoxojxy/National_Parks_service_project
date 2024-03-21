import json

# Define restaurant data
restaurant_data = [
    {
        "name": "16th Avenue Diner",
        "cuisine": "American",
        "location": "207 NE 16th Ave, Gainesville",
        "price_range": "$",
        "dietary_options": ["Vegetarian", "Vegan"],
        "dress_code": "Casual",
        "ratings": 4.2
        'menu': 'x'
    },
    {
        "name": "4 Rivers Smokehouse – Gainesville",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "43rd St Deli & Breakfast – South",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "43rd St Deli & Breakfast – West",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "4 Rivers Smokehouse – Gainesville",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "4th Ave Food Park",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "A’xin Mahzu Sushi & Grill",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Adam’s Rib Co. North",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "afternoon",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Airstream – Opus Coffee",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Alpin Bistro",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Amelia’s Italian Cuisine",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Bagel Bakery",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
]

# Specify the file path where you want to save the JSON file
file_path = 'restaurants.json'

# Write restaurant data to JSON file
with open(file_path, 'w') as json_file:
    json.dump(restaurant_data, json_file, indent=4)

print(f"JSON data has been saved to {file_path}")
