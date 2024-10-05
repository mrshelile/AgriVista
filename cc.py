import requests
import asyncio
from geopy.geocoders import Nominatim
import geocoder

class ModelData:
    def __init__(self, city, latitude, longitude, ph_level, soil_type):
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.soil_type = soil_type
        self.ph_level = ph_level
        self.conditions = []

        # API Keys for WorldWeather and OpenWeather
        self.api_key_worldweather = '61b0b632a8544dcb8bb93704242909'  # Replace with your World Weather Online API key
        self.api_key_openweather = '8a1b6e70490e41ddf5a53b131acbc60c'  # Replace with your OpenWeather API key
        
        # URLs to fetch weather data
        self.url_worldweather = f'http://api.worldweatheronline.com/premium/v1/weather.ashx?key={self.api_key_worldweather}&q={city}&fx=no&gb-defra-index=Band&format=json'
        self.url_openweather = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={self.api_key_openweather}&units=metric"
    
    async def get_model_data(self):
        # Fetch weather data from World Weather Online
        try:
            response = requests.get(self.url_worldweather)
            response.raise_for_status()
            data1 = response.json()
        except requests.exceptions.RequestException as e:
            print(f"WorldWeatherOnline Error: {e}")
            return

        # Fetch weather data from OpenWeather
        try:
            response = requests.get(self.url_openweather)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"OpenWeather Error: {e}")
            return

        # Extract weather conditions from OpenWeather
        humidity = data['main']['humidity']
        
        # Extract weather conditions from WorldWeather
        try:
            avrainfall = float(data1['data']['ClimateAverages'][0]['month'][8]['avgDailyRainfall'])  # Avg rainfall in September (8th month)
            ava_temperature = float(data1['data']['current_condition'][0]['temp_C'])
        except (KeyError, IndexError) as e:
            print(f"Data extraction error: {e}")
            return

        # Combine the fetched data into new_conditions
        new_conditions = [[ava_temperature, avrainfall * 30, self.ph_level, humidity, 7, 1, self.soil_type]]  
        self.conditions = new_conditions
        
        print(f"New conditions: {new_conditions}")


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
async def get_current_location_async():
    g = geocoder.ip('me')
    if g.ok:
        latitude, longitude = g.latlng
        return latitude, longitude
    else:
        print("Unable to fetch location using geocoder.")
        return None, None

# Get city and village name from location
async def get_city_and_village():
    latitude, longitude = get_current_location()
    if latitude and longitude:
        geolocator = Nominatim(user_agent="GetLoc")
        location = geolocator.reverse((latitude, longitude), language='en')
        city = location.raw['address'].get('city') or location.raw['address'].get('town')
        village = location.raw['address'].get('village') or location.raw['address'].get('hamlet') or location.raw['address'].get('locality')
        return city, village, latitude, longitude
    else:
        return None, None, None, None

# Main execution flow
async def main():
    # Get current location
    lat, lon = await get_current_location_async()
    if lat and lon:
        print(f"Current Location: Latitude: {lat}, Longitude: {lon}")

        # Get city and village name
        city, village, lat, lon = await get_city_and_village()
        if city:
            print(f"City: {city}, Village: {village}, Latitude: {lat}, Longitude: {lon}")

            # Create ModelData object
            ph_level = 6.5  # Example pH level
            soil_type = "Loamy"  # Example soil type
            model_data = ModelData(city, lat, lon, ph_level, soil_type)

            # Fetch model data
            await model_data.get_model_data()
        else:
            print("Could not fetch city or village information.")
    else:
        print("Could not determine current location.")

asyncio.run(main())
    
