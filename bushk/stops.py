import requests
import json
from .errors import *


class abcStop:
    def __init__(self, id: str):
        self._data=json.loads(requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/stop/{id}").content.decode(encoding="utf-8"))
        if self._data == {}:
            raise StopNotFound("API have not give data of this stop['{self.id}']! API尚未給出此站['{self.id}']的資料!")
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
            self._data=json.loads(requests.get("https://data.etabus.gov.hk/v1/transport/kmb/stop/").content.decode(encoding="utf-8"))


    async def all(self):
        _list=[]
        for data in self._data["data"]:
            _list.append(abcStop(id=data["stop"]))
        return _list
    

    async def get(self, id: str=None, name: str=None):
        if (id == None and name == None) or (id != None and name != None):
            raise OptionError("You should only enter one data or you have not enter any data! 您只能輸入一項數據，或者您還沒有輸入任何數據！")
        if name != None:
            for stop in self.all():
                if name == stop.name["en"] or name == stop.name["tc"] or name == stop.name["sc"]:
                    return stop
        if id != None:
            for stop in self.all():
                if id == stop.id:
                    return stop
        raise StopNotFound("API cannot get stop! API無法取得巴士站!")