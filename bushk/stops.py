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
    def __init__(self):
        self._data=json.loads(requests.get("https://data.etabus.gov.hk/v1/transport/kmb/stop/").content.decode(encoding="utf-8"))
        self.all=[]
        for data in self._data["data"]:
            self.all.append(abcStop(data))
    

    def get(self, id: str=None, name: str=None):
        if (id == None and name == None) or (id != None and name != None):
            raise OptionError("You should only enter one data or you have not enter any data! 您只能輸入一項數據，或者您還沒有輸入任何數據！")
        if name != None:
            for stop in self.all:
                if name == stop.name["en"] or name == stop.name["tc"] or name == stop.name["sc"]:
                    return stop
        if id != None:
            for stop in self.all:
                if id == stop.id:
                    return stop
        raise StopNotFound("API cannot get stop! API無法取得巴士站!")