import requests
import json

from omnibus.transloc.transloc import Transloc


class Stops(Transloc):

    def __init__(self):
        super(Stops, self).__init__()
        self.url = "https://transloc-api-1-2.p.rapidapi.com/stops.json"

    def get_stops(self):
        querystring = {"callback": "call", "agencies": self.agency_id}
        response = requests.request(
            "GET", self.url, headers=self.headers, params=querystring)
        resp_json = json.loads(response.text)
        #print(json.dumps(resp_json, indent=4))
        shortened_dict_list = []
        for stop_info in resp_json['data']:
            lat_lon_tuple = (stop_info['location']
                             ['lat'], stop_info['location']['lng'])
            shortened_dict = {"name": stop_info['name'], "stop_id": stop_info['stop_id'],
                              "location": lat_lon_tuple, "routes": stop_info['routes']}
            shortened_dict_list.append(shortened_dict)
        return shortened_dict_list
