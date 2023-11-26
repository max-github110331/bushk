import requests
import json
from .stops import Stops
from .errors import *


class abcRoute:
    def __init__(self, data):
        self.route=data["route"]
        self.service_type=data["service_type"]
        if self.service_type == "1":
            self.normal=True
        else:
            self.normal=False
        self.bound=data["bound"]
        self.stops={}
        for stop in json.loads(requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route-stop").content.decode("utf-8"))["data"]:
            if stop["route"] == self.route and stop["bound"] == self.bound and stop["service_type"] == self.service_type:
                self.stops[stop["seq"]]=stop["stop"]


class Routes:
    def __init__(self):
        self._data=json.loads(requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route/").content.decode("utf-8"))
        self.all=[]
        for data in self._data["data"]:
            self.all.append(abcRoute(data))


    def get(self, route: str, service_type: str="1"):
        _data=json.loads(requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/route/{route}/inbound/{service_type}").content.decode(encoding="utf-8"))
        if "code" in _data:
            raise RouteNotFound("API cannot get route! API無法取得路線!")
        elif _data["data"] == {}:
            raise RouteNotFound("API cannot get route! API無法取得路線!")
        else:
            return abcRoute(_data["data"])