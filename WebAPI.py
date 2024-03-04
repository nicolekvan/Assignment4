# webapi.py

# Nicole Kwan
# nkwan3@uci.edu
# 76647093

# A base class module that provides access to common features for your API modules

from abc import ABC, abstractmethod

class WebAPI(ABC):

  def _download_url(self, url: str) -> dict:
    #TODO: Implement web api request code in a way that supports
    # all types of web APIs
    pass

  def set_apikey(self, apikey:str) -> None:
    pass

  @abstractmethod
  def load_data(self):
    pass

  @abstractmethod
  def transclude(self, message:str) -> str:
    pass
