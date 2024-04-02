import json

# Define restaurant data
restaurant_data = [
    {
        "name": "16th Avenue Diner",
        "cuisine": "American",
        "location": "207 NE 16th Ave, Gainesville",
        "price_range": "$",
        "dietary_options": [],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "4 Rivers Smokehouse – Gainesville",
        "cuisine": "Barbecue",
        "location": "3262 sw 35th blvd, Gainesville",
        "distance": "",
        "price_range": "$$",
        "dietary_options": ["Vegan","Vegetarian"],
        "dress_code": "Casual Dress",
        "ratings": 4.2
    },
    {
        "name": "43rd St Deli & Breakfast – South",
        "cuisine": "American",
        "location": "3483 SW Williston Rd., Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "43rd St Deli & Breakfast – West",
        "cuisine": "American",
        "location": "4410 NW 25th Pl, Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "4th Ave Food Park",
        "cuisine": "Various",
        "location": "409 SW 4th Ave, Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.7
    },
    {
        "name": "A’xin Mahzu Sushi & Grill",
        "cuisine": "Sushi",
        "location": "5150 SW 34th St, Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.6
    },
    {
        "name": "Adam’s Rib Co. North",
        "cuisine": "Barbecue",
        "location": "2109 NW 13th St, Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "afternoon",
        "cuisine": "American, Breakfast",
        "location": "231 NW 10th ave, Gainesville",
        "distance": "",
        "price_range": "$$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.4
    },
    {
        "name": "Airstream – Opus Coffee",
        "cuisine": "Coffee",
        "location": "403 SW4th Ave, Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": [],
        "dress_code": "Casual",
        "ratings": 4.8
    },
    {
        "name": "Alpin Bistro",
        "cuisine": "French",
        "location": "15 SW 2nd St, Gainesville",
        "distance": "",
        "price_range": "$$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.3
    },
    {
        "name": "Amelia’s Italian Cuisine",
        "cuisine": "Italian",
        "location": "235 S Main St, Suite 107, Gainesville",
        "distance": "",
        "price_range": "$$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Dressy Casual",
        "ratings": 4.2
    },
    {
        "name": "Bagel Bakery",
        "cuisine": "Bagel",
        "location": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Bageland Bagels",
        "cuisine": "Bagel",
        "location": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "BagelS & Noodles",
        "cuisine": "Bagel",
        "location": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Bahama Breeze",
        "cuisine": "Caribbean",
        "location": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Ballyhoo",
        "cuisine": "Bar & Grill",
        "location": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Blackadder Brewing",
        "cuisine": "Brewery",
        "location": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },{
        "name": "Blue Gill Quality Foods",
        "cuisine": "Southern",
        "location": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
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
