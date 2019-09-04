from flask import Flask, render_template
from api_client import weather_api_client
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather/<city>')
def weather(city):
    wapi = weather_api_client()
    data = wapi.get_weather(city)

    datetime = format_datetime(data["dt"])
    weather = data["weather"][0]["main"]
    description = data["weather"][0]["description"]

    return render_template('weather.html', ct=city, dt=datetime, wt=weather, ds=description)


@app.route('/forecast/<city>')
def forecast(city):
    wapi = weather_api_client()
    data = wapi.get_forecast(city)

    return render_template('forecast.html', city_name=city, forecast_data=data)


def format_datetime(value):
    return datetime.fromtimestamp(value)


app.jinja_env.filters['format_datetime'] = format_datetime

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
