import requests
import json
from omnibus.transloc.transloc import Transloc

class Routes(Transloc):

    def __init__(self):
        super(Routes, self).__init__()
        self.url = "https://transloc-api-1-2.p.rapidapi.com/routes.json"

    def get_shuttle_routes(self):
        querystring = {"callback": "call", "agencies": self.agency_id}
        response = requests.request(
            "GET", self.url, headers=self.headers, params=querystring)

        routes = json.loads(response.text)
        routes = routes['data']['1199']
        for l in routes:
            del l['segments']
        return routes

    def make_id_name_mapping(self):
        routes = self.get_shuttle_routes()
        id_name_map = {}
        for route in routes:
            id_name_map[route['route_id']] = route['short_name']
        return id_name_map