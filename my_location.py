import requests
from geopy.geocoders import Nominatim
import geocoder
import asyncio

# Get current location using IPAPI
def get_current_location():
    try:
        response = requests.get('https://ipapi.co/json/')
        response.raise_for_status()
        data = response.json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        if latitude and longitude:
            return latitude, longitude
        else:
            print("Unable to fetch location.")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None

# Async function to get current location using Geocoder
async def get_current_location1():
    g = geocoder.ip('me')
    if g.ok:
        latitude, longitude = g.latlng
        return latitude, longitude
    else:
        print("Unable to fetch location using geocoder.")
        return None, None

# Get city name using latitude and longitude
def get_city_name():
    latitude, longitude = get_current_location()
    if latitude and longitude:
        geolocator = Nominatim(user_agent="GetLoc")
        location = geolocator.reverse((latitude, longitude), language='en')
        city = location.raw['address'].get('city', '')
        return city
    else:
        return "Location not found."

# Async function to get city and village name
async def get_city_and_village():
    latitude, longitude = get_current_location()
    if latitude and longitude:
        geolocator = Nominatim(user_agent="GetLoc")
        location = geolocator.reverse((latitude, longitude), language='en')
        city = location.raw['address'].get('city') or location.raw['address'].get('town')
        village = location.raw['address'].get('village') or location.raw['address'].get('hamlet') or location.raw['address'].get('locality')
        print(location.raw['address'])
        return city, latitude, longitude
    else:
        return None, None, None

# Reverse geocode latitude and longitude to get city name
def reverse_geocode(latitude, longitude):
    try:
        geolocator = Nominatim(user_agent="GetLoc")
        location = geolocator.reverse((latitude, longitude), language='en')
        if location and 'address' in location.raw:
            city = location.raw['address'].get('city') or location.raw['address'].get('town') or location.raw['address'].get('village')
            return city if city else "City not found."
        else:
            return "Location not found."
    except Exception as e:
        return f"Error: {e}"

# Get village from coordinates using reverse geocoding
def get_village():
    lat, lon = get_current_location()
    if lat and lon:
        url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            village = data.get('address', {}).get('village', 'Not found')
            return village
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
    else:
        return "Location not found."

# Helper to run async functions in the main thread
def main():
    # Run async function get_current_location1
    lat, lon = asyncio.run(get_current_location1())
    if lat and lon:
        print(f"Async Location: Latitude: {lat}, Longitude: {lon}")

    # Get city name
    city_name = get_city_name()
    print(f"City: {city_name}")
    
    # Run async function get_city_and_village
    city, lat, lon = asyncio.run(get_city_and_village())
    if city:
        print(f"City: {city}, Latitude: {lat}, Longitude: {lon}")
    
    # Get village
    village = get_village()
    print(f"Village: {village}")

main()
    
