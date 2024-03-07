# openweather.py

# Nicole Kwan
# nkwan3@uci.edu
# 76647093

# A module for interacting with the OpenWeather API
# API KEY: 510bd492cb913279a6869bd146ca2a62

import urllib, json
from urllib import request, error

class OpenWeather():
    def __init__(self, zipcode, ccode):
        self.zipcode = zipcode
        self.ccode = ccode

    def _download_url(self, url_to_download: str) -> dict:
        response = None
        r_obj = None

        try:
            response = urllib.request.urlopen(url_to_download)
            json_results = response.read()
            r_obj = json.loads(json_results)

        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))
        except urllib.error.URLError as e:
            print("Error: Failed to connect to the remote API: ", e)
        except ValueError as e:
            print("Error: ", e)

        finally:
            if response != None:
                response.close()
        
        return r_obj

    def set_apikey(self, apikey:str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
        '''
        #TODO: assign apikey value to a class data attribute that can be accessed by class members

        self.apikey = apikey
        return self.apikey

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
        self.wind = weather_obj["wind"]["speeed"]
        self.city = weather_obj["name"]
        self.sunset = weather_obj["sys"]["sunset"]

        return weather_obj