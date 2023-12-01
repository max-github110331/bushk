import requests
import json
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
        self.stops_id={}
        for stop in json.loads(requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route-stop").content.decode("utf-8"))["data"]:
            if stop["route"] == self.route and stop["bound"] == self.bound and stop["service_type"] == self.service_type:
                self.stops_id[stop["seq"]]=stop["stop"]


class Routes:
    def get(route: str, bound: str="O", service_type: str="1"):
        match bound.lower():
            case "o":
                bound="outbound"
            case "outbound":
                bound="outbound"
            case "ob":
                bound="outbound"
            case "i":
                bound="inbound"
            case "inbound":
                bound="inbound"
            case "ib":
                bound="inbound"
            case _:
                raise BoundError("Bound does not follow the format! Bound不遵循格式!")
        _data=json.loads(requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/route/{route}/{bound}/{service_type}").content.decode(encoding="utf-8"))
        if "code" in _data:
            raise RouteNotFound("API cannot get route! API無法取得路線!")
        elif _data["data"] == {}:
            raise RouteNotFound("API cannot get route! API無法取得路線!")
        else:
            return abcRoute(_data["data"])
        

    def all():
        _data=json.loads(requests.get("https://data.etabus.gov.hk/v1/transport/kmb/route/").content.decode("utf-8"))
        _list=[]
        for _route_data in _data["data"]:
            _list.append({"route": _route_data["route"], "bound": _route_data["bound"], "service_type": _route_data["service_type"]})
        return _list