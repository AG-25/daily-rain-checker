# Rain Checker ☔☔☔☔
This program checks the weather forecast for a specified location and sends an SMS warning if rain is likely to occur on the day.

## Usage
The script was designed to be run automatically at the same time every 24 hours, e.g. in the morning so that the user receives an SMS if they should take an umbrella to work.   
<br>
One way this can be done is by uploading the script to a cloud hosting platform, such as python anywhere:  
* https://www.pythonanywhere.com/

## Installation
Download main.py, or clone the repository, and then install the twilio and requests modules using pip (see requirements.txt).  
<br>
The following environment variables should then be populated before running the program:  
* OPEN_WEATHER_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_PHONE_NUMBER - Values for these variables can be retrieved by signing up for the free open weather and Twilio APIs (URLs provided below).  
* RECIPIENT_PHONE_NUMBER - This is the phone number which SMS warnings should be sent to when rain is likely (e.g. the mobile number of the script user, with the country code included at the start).  


## Supporting Libraries and APIs
* OpenWeatherAPI (to access weather forecast data): https://openweathermap.org/  
* Twilio (for sending SMS messages): https://www.twilio.com/  

