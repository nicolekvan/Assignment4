# lastfm.py

# Nicole Kwan
# nkwan3@uci.edu
# 76647093

# A module for interacting with the Last.FM API
# API Key: 333f89108e46378e606ff438072d6d87

from WebAPI import WebAPI
import random
import urllib, json
from urllib import request, error

class LastFM(WebAPI):
    def __init__(self, artist):
        self.artist = artist

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
        '''
        self.base = "http://ws.audioscrobbler.com/2.0/"
        self.method = "artist.getTopTracks"

        url = f"{self.base}?method={self.method}&artist={self.artist}&api_key={self.apikey}&format=json"
        artist_data = self._download_url(url)

        top_tracks = []
        for item in artist_data["toptracks"]["track"]:
            top_tracks.append(item["name"])

        self.tracks = top_tracks

        return artist_data
    
    def transclude(self, message:str) -> str:
        word_list = message.split()  # Split the message into a list of words
        transcluded_msg = []
        for word in word_list:
            if "@lastfm" in word:
                if "." in word:
                    transcluded_msg.append(random.choice(self.tracks) + ".")
                else:
                    transcluded_msg.append(random.choice(self.tracks))
            else:
                transcluded_msg.append(word)
        
        j_msg = ' '.join(transcluded_msg)
        return j_msg
