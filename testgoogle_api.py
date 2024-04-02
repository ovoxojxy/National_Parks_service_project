import requests
from api_key import google_key

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

address = '1600 Amphitheatre Parkway, Mountain View, CA'
latitude, longitude = get_coordinates(address)

if latitude is not None and longitude is not None:
    print(f'Latitude: {latitude}, Longitude: {longitude}')
else:
    print("Unable to retrieve coordinates")