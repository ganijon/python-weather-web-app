from flask import Flask
from api_client import weather_api_client

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'

@app.route('/weather')
def weather():
    
    api_url = 'api.openweathermap.org/data/2.5/'
    api_key = '623af9cc19f6aab782588ed432ed3434'
    wapi = weather_api_client(api_url, api_key)

    return wapi.get_weather('Boston')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')