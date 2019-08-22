from flask import Flask
from api_client import weather_api_client

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'

@app.route('/weather')
def weather(self):
    
    wapi = weather_api_client()
    return wapi.get_weather('Boston,US')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')