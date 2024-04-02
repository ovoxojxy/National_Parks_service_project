import requests
import sys

def get_user_location():
    try: 
        response = requests.get('https://ip-api.com/json/')
        data = response.json()
        if data['status'] == 'success':
            return data['lat'], data['lon']
    except Exception as e:
        print('Error getting user location:',e)
    return None, None

def main():
    user_latitude, user_longitude = get_user_location()
    if user_latitude is not None and user_longitude is not None:
        print(f"User's Location: Latitude {user_latitude}, Longitude {user_longitude}")
    else:
        print("Unable to retireve user location")

if __name__ == '__main__':
    main()