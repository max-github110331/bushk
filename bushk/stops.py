import requests
import json
from .errrors import *


class abcStop:
    def __init__(self, id: str):
        self._data=json.loads(requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/stop/{id}").content.decode(encoding="utf-8"))
        if self._data == {}:
            raise StopNotFound("API have not give data of this stop['{self.id}']!")
        self.id=self._data["data"]["stop"]
        self.name={
            "en": self._data["data"]["name_en"],
            "tc": self._data["data"]["name_tc"],
            "sc": self._data["data"]["name_sc"]
        }


    def __str__(self):
        return self.name["tc"]


class Stops:
    def __init__(self):
            pass