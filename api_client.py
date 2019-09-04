import requests

class weather_api_client:
    def __init__(self):
        self.url_base = 'api.openweathermap.org/data/2.5/'
        self.api_key = '623af9cc19f6aab782588ed432ed3434'

    def get_weather(self, city_name):
        response = requests.get(f'https://{self.url_base}weather?q={city_name}&appId={self.api_key}')
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def get_forecast(self, city_name):
        response = requests.get(f'https://{self.url_base}forecast?q={city_name}&appId={self.api_key}')
        if response.status_code == 200:
            return response.json()
        else:
            return response.text
