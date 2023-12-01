import requests
import json
from .routes import abcRoute
from .stops import abcStop
from .errors import *


class ETA:
    def get_route_stop(route: abcStop, stop: abcStop):
        _data=json.loads(requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/eta/{stop.id}/{route.route}/{route.service_type}").content.decode("utf-8"))
        _list=[]
        for _data in _data["data"]:
            _list.append({"arrive_at": _data["eta"].replace("T", " ")[:-6], "seq": _data["seq"], "rmk": {"tc": _data["rmk_tc"], "sc": _data["rmk_sc"], "en": _data["rmk_en"]}})
        return _list
    

    def get_stop(stop: abcStop):
        _data=json.loads(requests.get(f"https://data.etabus.gov.hk/v1/transport/kmb/stop-eta/{stop.id}").content.decode("utf-8"))
        _list=[]
        for _route_data in _data["data"]:
            _list.append({"route": _route_data["route"], "bound": _route_data["bound"], "service_type": _route_data["service_type"], "arrive_at": _data["eta"].replace("T", " ")[:-6], "seq": _data["seq"], "rmk": {"tc": _data["rmk_tc"], "sc": _data["rmk_sc"], "en": _data["rmk_en"]}})