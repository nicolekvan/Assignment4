import ds_client
server = "168.235.86.101" # replace with actual server ip address
port = 3021 # replace with actual port

from OpenWeather import OpenWeather 
from LastFM import LastFM
#ds_client.send(server, port, "bicole", "pwd123", "Hello World!")
fm = LastFM("The+Weeknd")
fm.set_apikey("333f89108e46378e606ff438072d6d87")  # Set the API key
fm.load_data()

weather = OpenWeather(94606, "US")
weather.set_apikey("510bd492cb913279a6869bd146ca2a62")
weather.load_data()
text = "the city is @city and the weather is @weather, my favorite artist is the weeknd and one of his top songs is @lastfm"
replaced_text = fm.transclude(text)
weather_text = weather.transclude(replaced_text)
print(weather_text)

#ds_client.send(server, port, "bicole", "pwd123", replaced_text)

"""artist = input("Enter your favorite artist: ").split()
zip = int(input("Enter your zip code: "))
if len(artist) > 1:
    send = "+".join(artist).title()
else:
    send = " ".join(artist)
print(send)"""