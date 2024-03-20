import json

# Define restaurant data
restaurant_data = [
    {
        "name": "Restaurant One",
        "cuisine": "Italian",
        "location": "123 Main St",
        "distance": "1 mile",
        "price_range": "$$",
        "dietary_options": ["Vegetarian", "Vegan"],
        "dress_code": "Casual",
        "ratings": 4.2
    },
    {
        "name": "Restaurant Two",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    }
]

# Specify the file path where you want to save the JSON file
file_path = 'restaurants.json'

# Write restaurant data to JSON file
with open(file_path, 'w') as json_file:
    json.dump(restaurant_data, json_file, indent=4)

print(f"JSON data has been saved to {file_path}")
