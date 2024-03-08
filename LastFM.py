# lastfm.py

# Nicole Kwan
# nkwan3@uci.edu
# 76647093

# A module for interacting with the Last.FM API
# API Key: 333f89108e46378e606ff438072d6d87

import urllib, json
from urllib import request, error

class LastFM():
    def __init__(self, artist):
        self.artist = artist


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
    