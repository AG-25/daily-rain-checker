# Rain Checker ☔☔☔☔
This program checks the weather forecast for a specified location and sends an SMS warning if rain is likely to occur that day.

## Usage
The script was designed to be run automatically at the same time every 24 hours, e.g. in the morning so that the user receives an SMS if they should take an umbrella to work. 
<br>
One way this can be done is by uploading the script to a cloud hosting platform, such as python anywhere:  
https://www.pythonanywhere.com/

## Installation
Download main.py and install the modules listed in requirements.txt using pip (twilio and requests).  
The following environment variables should then be populated before running the program:  
1.) OPEN_WEATHER_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_PHONE_NUMBER - Values for these variables can be retrieved by signing up for the free open weather and Twilio APIs (URLs provided below).  
2.) RECIPIENT_PHONE_NUMBER - This is the phone number that SMS warnings should be sent to when rain is likely (e.g. the mobile number of the script user, with the mobile country code included at the start).  


## Supporting Libraries and APIs
OpenWeatherAPI (to access weather forecast data): https://openweathermap.org/  
Twilio (for sending SMS messages): https://www.twilio.com/  

## Future Development  
I do not have any plans to develop this application in the future.

