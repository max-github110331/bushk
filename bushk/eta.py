import requests
import json
from .routes import abcRoute
from .stops import abcStop
from .errors import *


class abcETA:
    def __init__(self, data):
        self.company=data["co"]
        self.route=data["route"]
        self.bound=data["dir"]
        self.direction=data["dir"]
        self.service_type=str(data["service_type"])
        if data["eta"] == None:
            self.arrive_at="No Service"
        else:
            self.arrive_at=data["eta"].replace("T", " ")[:-6]
        self.sequence=str(data["eta_seq"])
        self.seq=self.sequence
        self.remark={
            "en": data["rmk_en"],
            "tc": data["rmk_tc"],
            "sc": data["rmk_sc"]
        }
        self.rmk=self.remark
        self.destination={
            "tc": data["dest_tc"],
            "en": data["dest_en"],
            "sc": data["dest_sc"]
        }
        self.dest=self.destination


class ETA:
    def get_route_stop(route: abcStop, stop: abcStop):
        _data=json.loads(requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/eta/{stop.id}/{route.route}/{route.service_type}").content.decode("utf-8"))
        _list=[]
        for _data in _data["data"]:
            _list.append(abcETA(_data))
        return _list
    

    def get_stop(stop: abcStop):
        _data=json.loads(requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/stop-eta/{stop.id}").content.decode("utf-8"))
        _list=[]
        for _route_data in _data["data"]:
            _list.append(abcETA(_route_data))
        return _list
    

    def get_route(route: abcStop):
        _data=json.loads(requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/route-eta/{route.route}/{route.service_type}").content.decode("utf-8"))
        _list=[]
        for _route_data in _data["data"]:
            _list.append(abcETA(_route_data))
        return _list