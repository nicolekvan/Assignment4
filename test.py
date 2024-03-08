import ds_client
server = "168.235.86.101" # replace with actual server ip address
port = 3021 # replace with actual port

from OpenWeather import OpenWeather 
from LastFM import LastFM
#ds_client.send(server, port, "bicole", "pwd123", "Hello World!")
fm = LastFM("The+Weeknd")
fm.set_apikey("333f89108e46378e606ff438072d6d87")  # Set the API key
fm.load_data()
text = "my favorite artist is the weeknd and one of his top songs is @lastfm"
replaced_text = fm.transclude(text)
print(replaced_text)

#ds_client.send(server, port, "bicole", "pwd123", replaced_text)
