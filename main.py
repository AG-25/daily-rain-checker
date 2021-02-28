import requests
import os
from twilio.rest import Client

# The latitude and longitude of the location where weather should be monitored
LOCATION_LAT = '52.520008'
LOCATION_LONG = '13.404954'

# API keys and Twilio account details (see readme)
OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_ACCOUNT_PHONE_NUMBER = os.getenv('TWILIO_ACCOUNT_PHONE_NUMBER')

# Phone number which SMS rain warnings should be sent to
RECIPIENT_PHONE_NUMBER = os.getenv('RECIPIENT_PHONE_NUMBER')

OPEN_WEATHER_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
parameters = {
    'lat': LOCATION_LAT,
    'lon': LOCATION_LONG,
    'appid': OPEN_WEATHER_API_KEY,
    'exclude': 'current,minutely,daily'
}

# Get weather forecast for the next 12 hours from the Open weather API
response = requests.get(OPEN_WEATHER_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

hourly_weather_codes = [
    hour['weather'][0]['id'] for hour in weather_data['hourly'][:12]
]

# Check weather codes to see if rain is likely
will_rain = False
for code in hourly_weather_codes:
    if int(code) < 700:
        print('rain is likely')
        will_rain = True
        break

# Send an SMS to the user if rain is likely
if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain, bring an umbrella",
        from_=TWILIO_ACCOUNT_PHONE_NUMBER,
        to=RECIPIENT_PHONE_NUMBER,
    )
    print(message.status)
