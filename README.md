This program checks the weather forecast for a specified location and sends an SMS warning if rain is likely to occur on the day.

The script was designed to be run automatically at the same time every day, e.g. in the morning so that the user receives an SMS if they should take an umbrella to work. One way this can be done is by uploading the script to a cloud hosting platform, such as python anywhere:  
https://www.pythonanywhere.com/

Two free APIs are used by the program:  
OpenWeatherAPI (to access weather forecast data): https://openweathermap.org/  
Twilio (for sending SMS messages): https://www.twilio.com/  

The following environment variables need to be provided for the script to work:  
OPEN_WEATHER_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_PHONE_NUMBER - These can be retrieved by signing up for the free APIs at the URLs provided above.  
RECIPIENT_PHONE_NUMBER - This is the phone number that SMS warnings should be sent to when rain is likely (e.g. the mobile number of the script user).  

The user should also provide the latitude and longitude of the location they wish for the weather to monitored at.  
