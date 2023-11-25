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
        self.orig_stop=Stops().get(name=data["orig_en"])
        self.dest_stop=Stops().get(name=data["dest_en"])


class Route:
    def __init__(self):
        self._data=json.loads(requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route/").content.decode("utf-8"))
        self.all=[]
        for data in self._data["data"]:
            self.all.append(abcRoute(data))


    def get(self, route: str, bound: str="O", service_type: str="1"):
        for route in self.all:
            if route.route == route and route.bound == bound and route.service_type == service_type:
                return route
        raise RouteNotFound("API cannot get route! API無法取得路線!")