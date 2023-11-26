import requests
import json
from .errors import *


class abcStop:
    def __init__(self, data):
        self.id=data["stop"]
        self.name={
            "en": data["name_en"],
            "tc": data["name_tc"],
            "sc": data["name_sc"]
        }


class Stops:
    def get(id: str):
        _data=json.loads(requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/stop/{id}").content.decode(encoding="utf-8"))
        if _data["data"] == {}:
            raise StopNotFound("API cannot get stop! API無法取得巴士站!")
        else:
            return abcStop(_data["data"])