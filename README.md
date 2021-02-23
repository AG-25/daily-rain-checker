A script that checks the weather forecast for a specified location and then sends an SMS warning if rain is likely to occur on the day.

The script was designed to be run automatically at the same time every day, e.g. in the morning so that the user receives an SMS if they should take an umbrella to work. One way this can be done is by uploading the script to a cloud hosting platform, such as python anywhere:  
https://www.pythonanywhere.com/


Two APIs are used in the script:  
OpenWeatherAPI (to access weather forecast data): https://openweathermap.org/  
Twilio (for sending SMS messages): https://www.twilio.com/  

To get the script working, an OpenWeather API key, Twilio account sid and Twilio auth token must be provided as environment variables (sign-up is free using the links provided above).

The user should also enter the latitude/ longitude of the location they wish to check the weather at, and the mobile number they wish to receive an SMS warning to when rain is likely.
