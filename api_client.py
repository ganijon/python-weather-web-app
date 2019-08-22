import http.client
import json

class weather_api_client:
    def __init__(self, api_url_base, api_key):
        self.api_url_base = api_url_base
        self.api_key = api_key
    
    def get_weather(self, city_name):
        
        #api_url = '{0}weather?q={1}'.format(self.api_url_base, city_name)
        #connection = http.client.HTTPConnection(self.api_url_base, 80, timeout=10)
        
        connection = http.client.HTTPConnection('api.openweathermap.org/data/2.5/weather?q=Boston', 80, timeout=10)

        headers = {'Content-Type': 'application/json',
           'Authorization': 'appid {0}'.format(self.api_key)}
                
        connection.request("GET", '/', json.dumps(headers))

        response = connection.getresponse()

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return response.content