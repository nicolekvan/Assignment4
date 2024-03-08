# webapi.py

# Nicole Kwan
# nkwan3@uci.edu
# 76647093

# A base class module that provides access to common features for your API modules

from abc import ABC, abstractmethod
import json
import urllib

class WebAPI(ABC):

  def _download_url(self, url: str) -> dict:
    #TODO: Implement web api request code in a way that supports
    # all types of web APIs

    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url)
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
    self.apikey = apikey

  @abstractmethod
  def load_data(self):
    pass

  @abstractmethod
  def transclude(self, message:str) -> str:
    pass
