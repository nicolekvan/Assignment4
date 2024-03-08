"""import urllib, json
from urllib import request,error

def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))

    finally:
        if response != None:
            response.close()
    
    return r_obj

def main() -> None:
    zip = "94606"
    ccode = "US"
    apikey = "510bd492cb913279a6869bd146ca2a62"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip},{ccode}&appid={apikey}"

    weather_obj = _download_url(url)
    if weather_obj is not None:
        print(weather_obj['weather'][0]['description'])
        print(weather_obj)

if __name__ == '__main__':
    main()"""

"""from OpenWeather import OpenWeather

weather = OpenWeather("92844", "US")

x = weather.set_apikey("510bd492cb913279a6869bd146ca2a62")
print(x)
weather.load_data()"""

from OpenWeather import OpenWeather

zipcode = "92697"
ccode = "US"
apikey = "510bd492cb913279a6869bd146ca2a62"

open_weather = OpenWeather(zipcode, ccode)
open_weather.set_apikey(apikey)
open_weather.load_data()

print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
print(f"The current weather for {zipcode} is {open_weather.description}")
print(f"The current humidity for {zipcode} is {open_weather.humidity}")
print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")

from LastFM import LastFM

lastfm = LastFM("Drake")
lastfm.set_apikey("333f89108e46378e606ff438072d6d87")
lastfm.load_data()
print(lastfm.tracks)