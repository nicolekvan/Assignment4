# openweather.py

# Nicole Kwan
# nkwan3@uci.edu
# 76647093

# A module for interacting with the OpenWeather API

from WebAPI import WebAPI
import urllib, json
from urllib import request, error

class OpenWeather(WebAPI):
    def __init__(self, zipcode="92617", ccode="US"):
        self.zipcode = zipcode
        self.ccode = ccode

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
        '''

        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}"
        weather_obj = self._download_url(url)
        
        self.temperature = weather_obj["main"]["temp"]
        self.high_temperature = weather_obj["main"]["temp_max"]
        self.low_temperature = weather_obj["main"]["temp_min"]
        self.feels_like = weather_obj["main"]["feels_like"]
        self.longitude = weather_obj["coord"]["lon"]
        self.latitude = weather_obj["coord"]["lat"]
        self.description = weather_obj["weather"][0]["description"]
        self.humidity = weather_obj["main"]["humidity"]
        self.wind = weather_obj["wind"]["speed"]
        self.city = weather_obj["name"]
        self.sunset = weather_obj["sys"]["sunset"]

        return weather_obj
    
    def transclude(self, message:str) -> str:
        word_list = message.split()  # Split the message into a list of words
        transcluded_msg = []
        for word in word_list:
            if "@weather" in word:
                if "." in word:
                    transcluded_msg.append(self.description + ".")
                elif "," in word:
                    transcluded_msg.append(self.description + ",")
                elif "!" in word:
                    transcluded_msg.append(self.description + "!")
                else:
                    transcluded_msg.append(self.description)
            elif "@temperature" in word:
                if "." in word:
                    transcluded_msg.append(str(self.temperature) + ".")
                elif "," in word:
                    transcluded_msg.append(str(self.temperature) + ",")
                elif "!" in word:
                    transcluded_msg.append(str(self.temperature) + "!")
                else:
                    transcluded_msg.append(str(self.temperature))
            elif "@city" in word:
                if "." in word:
                    transcluded_msg.append(self.city + ".")
                elif "," in word:
                    transcluded_msg.append(self.city + ",")
                elif "!" in word:
                    transcluded_msg.append(self.city + "!")
                else:
                    transcluded_msg.append(self.city)
            else:
                transcluded_msg.append(word)
        
        j_msg = ' '.join(transcluded_msg)
        return j_msg

