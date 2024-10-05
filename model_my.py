import requests
import asyncio

class ModelData:
    def __init__(self, city, latitude, longitude, ph_level, soil_type):
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.soil_type = soil_type
        self.ph_level = ph_level
        self.conditions = []

        # API Keys for worldweather and openweather
        api_key = '61b0b632a8544dcb8bb93704242909' # Replace with your World Weather Online API key
        api_key1 = '8a1b6e70490e41ddf5a53b131acbc60c' # Replace with your OpenWeather API key
        
        # URLs to fetch weather data
        self.url = f'http://api.worldweatheronline.com/premium/v1/weather.ashx?key={api_key}&q={city}&fx=no&gb-defra-index=Band&format=json'  # worldweather
        self.URL = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key1}&units=metric"  # open weather
    
    async def getModelData(self):
        # Fetch weather data from World Weather Online
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for any bad response
            data1 = response.json()
        except requests.exceptions.RequestException as e:
            print(f"WorldWeatherOnline Error: {e}")
            return

        # Fetch weather data from OpenWeather
        try:
            response = requests.get(self.URL)
            response.raise_for_status()  # Raise an exception for any bad response
            data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"OpenWeather Error: {e}")
            return

        # Extract weather conditions from OpenWeather
        humidity = data['main']['humidity']
        
        # Extract weather conditions from WorldWeather
        try:
            avrainfall = float(data1['data']['ClimateAverages'][0]['month'][8]['avgDailyRainfall'])  # Avg rainfall in September (8th month)
            ava_temparature = float(data1['data']['current_condition'][0]['temp_C'])
        except (KeyError, IndexError) as e:
            print(f"Data extraction error: {e}")
            return

        # Example: Combine the fetched data into new_conditions
        new_conditions = [[ava_temparature, avrainfall * 30, self.ph_level, humidity, 7, 1, self.soil_type]]  
        self.conditions = new_conditions
        
        print(f"New conditions: {new_conditions}")


# Helper function to run async function in main thread
def main():
    # Replace with actual values
    city = "Maseru"
    latitude = -29.3167
    longitude = 27.4833
    ph_level = 6.5
    soil_type = "Loamy"

    # Create ModelData object
    model_data = ModelData(city, latitude, longitude, ph_level, soil_type)

    # Run async function to fetch weather data
    asyncio.run(model_data.getModelData())

main()

