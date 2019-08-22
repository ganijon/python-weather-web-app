from flask import Flask, render_template
from api_client import weather_api_client
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather/<city>')
def weather(city):

    wapi = weather_api_client()
    # data = wapi.get_weather(city)

    # read file
    with open('sample_data.json', 'r') as myfile:
        data = myfile.read()

    return render_template('weather.html', city_name=city, weather_data=json.loads(data))


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
